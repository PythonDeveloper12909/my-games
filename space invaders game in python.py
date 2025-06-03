import pygame 
from sys import exit
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders Game")
background=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invaders background.jpg")
player=pygame.image.load("C:\\Users\\Ansh\Desktop\\images_game\\space invader player ship.xcf")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    screen.blit(player,(350,480))
    pygame.display.update()