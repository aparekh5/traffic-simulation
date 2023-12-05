import pygame
import time


GRASS_COLOR='#136d15'
ROAD_COLOR='#2f2f2f'
DOTTED_LINE_COLOR='#d2b746'

SIDE_LENGTH = 1000
EMPTY_SPACE_LENGTH = 450
DOTTED_LINE_WIDTH = 5
DOTTED_LINE_HEIGHT = 25

ROAD_LENGTH = SIDE_LENGTH - (EMPTY_SPACE_LENGTH*2)

pygame.init()
screen = pygame.display.set_mode((SIDE_LENGTH, SIDE_LENGTH))
clock = pygame.time.Clock()
running = True

# DRAW GRASS
pygame.draw.rect(screen, GRASS_COLOR, pygame.Rect(0, 0, EMPTY_SPACE_LENGTH, EMPTY_SPACE_LENGTH))
pygame.draw.rect(screen, GRASS_COLOR, pygame.Rect(EMPTY_SPACE_LENGTH+ROAD_LENGTH, 0, EMPTY_SPACE_LENGTH, EMPTY_SPACE_LENGTH))
pygame.draw.rect(screen, GRASS_COLOR, pygame.Rect(0, EMPTY_SPACE_LENGTH+ROAD_LENGTH, EMPTY_SPACE_LENGTH, EMPTY_SPACE_LENGTH))
pygame.draw.rect(screen, GRASS_COLOR, pygame.Rect(EMPTY_SPACE_LENGTH+ROAD_LENGTH, EMPTY_SPACE_LENGTH+ROAD_LENGTH, EMPTY_SPACE_LENGTH, EMPTY_SPACE_LENGTH))

# DRAW ROADS
pygame.draw.rect(screen, ROAD_COLOR, pygame.Rect(EMPTY_SPACE_LENGTH, 0, ROAD_LENGTH, SIDE_LENGTH))
pygame.draw.rect(screen, ROAD_COLOR, pygame.Rect(0, EMPTY_SPACE_LENGTH, SIDE_LENGTH, ROAD_LENGTH))

# DRAW DOTTED LINES
start = 0
while start < SIDE_LENGTH:
    pygame.draw.rect(screen, DOTTED_LINE_COLOR, pygame.Rect(EMPTY_SPACE_LENGTH+(ROAD_LENGTH-DOTTED_LINE_WIDTH)/2, start, DOTTED_LINE_WIDTH, DOTTED_LINE_HEIGHT))
    start += DOTTED_LINE_HEIGHT*2
start = 0
while start < SIDE_LENGTH:
    pygame.draw.rect(screen, DOTTED_LINE_COLOR, pygame.Rect(start, EMPTY_SPACE_LENGTH+(ROAD_LENGTH-DOTTED_LINE_WIDTH)/2, DOTTED_LINE_HEIGHT, DOTTED_LINE_WIDTH ))
    start += DOTTED_LINE_HEIGHT*2


 

 
pygame.display.flip()
clock.tick(60)
time.sleep(5)
pygame.quit()