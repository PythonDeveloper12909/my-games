import pygame 
from sys import exit
class Player:
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader player ship.xcf")
        self.rect=self.image.get_rect(midbottom=(400,555))
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.key.LEFT]:
            self.rect.x -= 5
        elif keys[pygame.key.RIGHT]:
            self.rect.x += 5 
        elif keys[pygame.key.UP]:
            self.rect.y -= 5
        elif keys[pygame.key.DOWN]:
            self.rect.y += 5
    def update(self):
        self.move()
pygame.init()
player=Player()
player_group=pygame.sprite.GroupSingle(player)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders Game")
background=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invaders background.jpg")
player=pygame.image.load("C:\\Users\\Ansh\Desktop\\images_game\\space invader player ship.xcf")
player_rect=player.get_rect(midbottom=(400,555))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    player_group.draw(screen)
    player_group.update()
    pygame.display.update()