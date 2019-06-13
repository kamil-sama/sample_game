import pygame
from pygame.locals import *
from resources.data import config

pygame.init()

data = {
    'screen' : pygame.display.set_mode((config.display['resolution']['width'], config.display['resolution']['height'])),
    'robo' : pygame.image.load("resources/images/robo.png"),
    'playerpos' : config.player['position']['start'],
    'keys' : [False, False, False, False] # keys= [W, A, S, D]
}





def quit():
    pygame.quit() 
    exit(0)

def handleMovementKeys():
    global data
    if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                data['keys'][0]=True
            elif event.key==K_a:
                data['keys'][1]=True
            elif event.key==K_s:
                data['keys'][2]=True
            elif event.key==K_d:
                data['keys'][3]=True

    if event.type == pygame.KEYUP:
        if event.key==pygame.K_w:
            data['keys'][0]=False
        elif event.key==pygame.K_a:
            data['keys'][1]=False
        elif event.key==pygame.K_s:
            data['keys'][2]=False
        elif event.key==pygame.K_d:
            data['keys'][3]=False

def handleMovement():
    global data

    if data['keys'][0]:
        data['playerpos'][1]-=2
    elif data['keys'][2]:
        data['playerpos'][1]+=2
    if data['keys'][1]:
        data['playerpos'][0]-=2
    elif data['keys'][3]:
        data['playerpos'][0]+=2


if __name__ == "__main__":
    while bool(True):
        data['screen'].fill(config.colours['white'])
        data['screen'].blit(data['robo'], data['playerpos'])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            
            handleMovementKeys()
        handleMovement()
    
    