# heroselection: Selects a hero at random

import sys, os, random, pygame
from pygame.locals import *

BOXSIZE = pic_wid = 80
pic_height = 80
num_heroes = 21
num_columns = 7
window_wid = 600
window_height = 600
BLUE = (  0,   0, 255)
GAPSIZE = 4
XMARGIN = 10
YMARGIN = 10
WAITTIME = 1500

def main():
    # Set up Game Constants
    pygame.init()
    clock = pygame.time.Clock()
    game_state = 0
    highlightBoxx = highlightBoxy = 0
    troll = 0


    # Set up the Window
    DISPLAYSURF = pygame.display.set_mode((window_wid, window_height), 0, 32)
    pygame.display.set_caption('Overwatch Hero Selector!')

    # Set up images
    images = loadHeroPics('Hero_Icon_', '.png', num_heroes, pic_wid, pic_height)
    
    # Main Game Loop
    while True:
        # No button has been pressed
        while game_state == 0: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        random.shuffle(images)
                    if event.key == K_RETURN:
                        game_state = 1
                        pygame.time.set_timer(USEREVENT+1, WAITTIME)
                        #random.shuffle(images)
                    if event.key == K_t:
                        game_state = 1
                        troll = 1
                        pygame.time.set_timer(USEREVENT+1, WAITTIME)

            DISPLAYSURF.fill((0,0,0))
            drawBoard(DISPLAYSURF, num_heroes, num_columns, images, pic_wid, pic_height)

            pygame.display.update()
            clock.tick()
        
        # Choose randomly
        while game_state == 1:
            highlightBoxx = random.randint(0,num_columns -1)
            highlightBoxy = random.randint(0,int(num_heroes/num_columns) -1)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT+1:
                    game_state = 2
            DISPLAYSURF.fill((0,0,0))
            if troll == 0:
                drawBoard(DISPLAYSURF, num_heroes, num_columns, images, pic_wid, pic_height)
            else:
                drawTroll(DISPLAYSURF, num_heroes, num_columns, images, pic_wid, pic_height, 7)
                
            drawHighlightBox(DISPLAYSURF, highlightBoxx,highlightBoxy)
            
            pygame.display.update()
            clock.tick()

        #finally chosen a winner
        while game_state == 2:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        game_state = 0
                        troll = 0
            DISPLAYSURF.fill((0,0,0))
            if troll == 0:
                drawBoard(DISPLAYSURF, num_heroes, num_columns, images, pic_wid, pic_height)
            else:
                drawTroll(DISPLAYSURF, num_heroes, num_columns, images, pic_wid, pic_height, 7)
                
            drawHighlightBox(DISPLAYSURF, highlightBoxx,highlightBoxy)

            
            pygame.display.update()
            clock.tick()

# Load up the files
def loadHeroPics(name, filetype, num_heroes, pic_wid, pic_height):
    images = [name + str(image+1) + filetype for image in range(num_heroes)]
    for i in range(num_heroes):
        images[i] = pygame.image.load(str(images[i]))
        images[i] = pygame.transform.scale(images[i], (int(pic_wid), int(pic_height)))
    return images

def drawBoard(surfaceboard, num_heroes, num_columns, images, pic_wid, pic_height):
    for i in range(int(num_heroes/num_columns)):
        for j in range(num_columns):
            surfaceboard.blit(images[int(j+(i*num_columns))], (j*(int(pic_wid)+GAPSIZE)+XMARGIN,i * (int(pic_height)+GAPSIZE)+YMARGIN))

def drawTroll(surfaceboard, num_heroes, num_columns, images, pic_wid, pic_height, troll):
    for i in range(int(num_heroes/num_columns)):
        for j in range(num_columns):
            surfaceboard.blit(images[troll], (j*(int(pic_wid)+GAPSIZE)+XMARGIN,i * (int(pic_height)+GAPSIZE)+YMARGIN))


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (pic_wid + GAPSIZE) + XMARGIN
    top = boxy * (pic_height + GAPSIZE) + YMARGIN
    return (left, top)

def drawHighlightBox(surfaceboard, boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(surfaceboard, BLUE, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


if __name__ == '__main__':
    main()
