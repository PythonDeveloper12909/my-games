import pygame 
from sys import exit
import random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader player ship.xcf")
        self.rect=self.image.get_rect(midbottom=(400,555))
        self.bullet=pygame.Surface((10, 30))
        self.bullet.fill((255, 255, 255))  
        self.bullet_rect=self.bullet.get_rect(midbottom=(400,555))
        self.bullet_rect.midbottom=self.rect.midtop
        self.width1=100
        self.width2=100
        self.health_indicator1=pygame.Surface((self.width1,15))
        self.health_indicator1.fill((0, 255, 0))
        self.health_indicator1_rect=self.health_indicator1.get_rect(topleft=(10, 10))
        self.health_indicator2=pygame.Surface((self.width2,15))
        self.health_indicator2.fill((255,0,0))
        self.health_indicator2_rect=self.health_indicator2.get_rect(topleft=(10, 10))
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
    def blit(self,surface):
        surface.blit(self.bullet, self.bullet_rect)
    def shoot(self):
        self.bullet_rect.y-=7
        if self.bullet_rect.y < 0:
            self.bullet_rect.midbottom=self.rect.midtop   
    def blit_health_indicator(self, surface):
        surface.blit(self.health_indicator2, self.health_indicator2_rect)
        surface.blit(self.health_indicator1, self.health_indicator1_rect)
    def health_indicator(self):
        self.health_indicator2_rect.midtop=self.rect.midbottom
        self.health_indicator1_rect.midtop=self.rect.midbottom
    def update(self):
        self.move()
        self.blit(screen)
        self.shoot()   
        self.blit_health_indicator(screen)
        self.health_indicator()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader blue enemy.xcf")
        self.rect=self.image.get_rect(midbottom=(450,-5))
        self.image2=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy yellow.xcf")
        self.rect2=self.image2.get_rect(midbottom=(350,-5))
        self.image3=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy pink.xcf")
        self.rect3=self.image3.get_rect(midbottom=(250,-5))
    def move(self):
        self.rect.y += 1
        self.rect2.y += 1
        self.rect3.y += 1
    def blit(self,surface):
        surface.blit(self.image2, self.rect2)
        surface.blit(self.image3, self.rect3)
    def kill1(self):
        if self.rect.x > 725 or self.rect.x < 50:
            self.kill()
        if self.rect2.x > 725 or self.rect2.x < 50:
            self.kill()
        if self.rect3.x > 725 or self.rect3.x < 50:
            self.kill()   
    def shoot_enemy(self, player):
        if player.bullet_rect.colliderect(self.rect): 
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect.y=800          
        elif player.bullet_rect.colliderect(self.rect2):
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect2.y=800
        elif player.bullet_rect.colliderect(self.rect3):
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect3.y=800 
    def health_indicator_low(self,player):
        if player.rect.colliderect(self.rect):
            player.width1=80      
        if player.rect.colliderect(self.rect2):
            player.width1=80
        if player.rect.colliderect(self.rect3):
            player.width1=80
    def update(self):
        self.move()
        self.blit(screen)
        self.kill1()
        self.shoot_enemy(player_group.sprite)
        self.health_indicator_low(player_group.sprite)
def spawn_enemy():
         enemy=Enemy()
         enemy_group.add(enemy)
         enemy.rect.x = random.randint(50, 725)
         enemy.rect2.x = random.randint(50, 725)
         enemy.rect3.x = random.randint(50, 725)
         if enemy.rect.colliderect(enemy.rect2) or enemy.rect.colliderect(enemy.rect3) or enemy.rect2.colliderect(enemy.rect3) or enemy.rect2.colliderect(enemy.rect) or enemy.rect3.colliderect(enemy.rect) or enemy.rect3.colliderect(enemy.rect2):
             enemy.rect.x = random.randint(50, 725)
             enemy.rect2.x = enemy.rect.x + 128
             enemy.rect3.x = enemy.rect.x - 100
        

pygame.init()
player=Player()
player_group=pygame.sprite.GroupSingle(player)
enemy=Enemy()
enemy_group=pygame.sprite.Group(enemy)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders Game")
background=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invaders background.jpg").convert_alpha()
player=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader player ship.xcf").convert_alpha()
player_rect=player.get_rect(midbottom=(400,555))
enemy_blue=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader blue enemy.xcf").convert_alpha()
enemy_pink=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy pink.xcf").convert_alpha()
enemy_yellow=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\space invader enemy yellow.xcf").convert_alpha()
bullet=pygame.Surface((10, 20))
bullet.fill((255, 0, 0))
bullet_rect=bullet.get_rect(midbottom=(400,555))
width1=100
width2=100
health_indicator1=pygame.Surface((width1,15))
health_indicator1.fill((0, 255, 0))
health_indicator1_rect=health_indicator1.get_rect(topleft=(10, 10))
health_indicator2=pygame.Surface((width2,15))
health_indicator2.fill((255,0,0))
health_indicator2_rect=health_indicator2.get_rect(topleft=(40, 10))
clock=pygame.time.Clock()
Userevent = pygame.USEREVENT + 1
pygame.time.set_timer(Userevent, 2500)  
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == Userevent:
            spawn_enemy()
    screen.blit(background,(0,0))
    player_group.draw(screen)
    enemy_group.draw(screen)
    player_group.update()
    enemy_group.update()
    pygame.display.update()
    clock.tick(60)