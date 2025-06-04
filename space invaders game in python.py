import pygame 
from sys import exit
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader player ship.xcf")
        self.rect=self.image.get_rect(midbottom=(400,555))
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 3 
        elif keys[pygame.K_UP]:
            self.rect.y -= 3
        elif keys[pygame.K_DOWN]:
            self.rect.y += 3
    def update(self):
        self.move()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader blue enemy.xcf")
        self.rect=self.image.get_rect(midbottom=(400,555))
        self.image2=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy yellow.xcf")
        self.rect2=self.image2.get_rect(midbottom=(400,555))
        self.image3=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy pink.xcf")
        self.rect3=self.image3.get_rect(midbottom=(400,555))
pygame.init()
player=Player()
player_group=pygame.sprite.GroupSingle(player)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders Game")
background=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invaders background.jpg").convert_alpha()
player=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader player ship.xcf").convert_alpha()
player_rect=player.get_rect(midbottom=(400,555))
enemy_blue=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader blue enemy.xcf").convert_alpha()
enemy_pink=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy pink.xcf").convert_alpha()
enemy_yellow=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy yellow.xcf").convert_alpha()
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    player_group.draw(screen)
    player_group.update()
    screen.blit(enemy_yellow,(400,100))
    screen.blit(enemy_pink,(300,100))
    screen.blit(enemy_blue,(500,100))
    pygame.display.update()
    clock.tick(60)