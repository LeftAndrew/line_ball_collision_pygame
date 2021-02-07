import pygame
import math 
SIZE = [800, 800]
screen = pygame.display.set_mode(SIZE)

BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
active = True
clock = pygame.time.Clock()
circle_pos = [0, 0]
line = [[200, 300], [300, 200]]

def dist(x1, y1, x2, y2):
    distance = math.sqrt(( ((x1 - x2) ** 2) + ((y1 - y2) ** 2) ))
    return distance
def point_line_collision(line, px, py):
    dist1 = dist(line[0][0], line[0][1], px, py) 
    dist2 = dist(line[1][0], line[1][1], px, py)

    lenght = dist(line[0][0], line[0][1], line[1][0], line[1][1])
    buffer = 5
    if dist1 + dist2 >= lenght - buffer and dist1 + dist2 <= lenght + buffer:
        return True
    else:
        return False              
    
    
def line_circle_collision(c, l):
    circle_rect = pygame.Rect(circle_pos[0] - 20, circle_pos[1] - 20, 40, 40)
    if circle_rect.collidepoint(line[0]) or circle_rect.collidepoint(line[1]):
        return True
    distx1 = l[0][0] - l[1][0]
    disty1 = l[0][1] - l[1][1]
    lenght = math.sqrt((distx1 * distx1) + ( disty1 * disty1))
    
    
    
    #lenght = dist(l[0][0], l[0][1], l[1][0], l[1][1])
    dot = ( ((c[0] - l[0][0]) * (l[1][0] - l[0][0])) + ((c[1] -l[0][1]) * (l[1][1] - l[0][1]))) / lenght ** 2 
    closestx = l[0][0] + (dot * (l[1][0] - l[0][0]))
    closesty = l[0][1] + (dot * (l[1][1] - l[0][1]))
        
    
    OnSegment = point_line_collision(l, closestx, closesty)
    if OnSegment != True:
        return False
    distx = closestx - c[0] 
    disty = closesty - c[1]
    distance = math.sqrt((distx * distx) + (disty * disty))    
    if distance <= 20:
        return True
    else:
        return False


while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    circle_pos[0] = pygame.mouse.get_pos()[0]
    circle_pos[1] = pygame.mouse.get_pos()[1]
    #DRAWING STUFF
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, circle_pos, 20)
    if line_circle_collision(circle_pos, line):
        pygame.draw.line(screen, RED, line[0], line[1], 4)
    else:
        pygame.draw.line(screen, GREEN, line[0], line[1], 4)

    
    pygame.display.flip()
            
