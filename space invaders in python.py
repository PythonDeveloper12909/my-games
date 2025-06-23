import pygame 
from sys import exit
import random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader player ship.xcf")
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
        self.game_over_font = pygame.font.SysFont("Arial", 100)
        self.game_over_text = self.game_over_font.render("Game Over", True, (255, 255,255))
        self.game_over_rect = self.game_over_text.get_rect(center=(400, 300))
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 4
        elif keys[pygame.K_UP]:
            self.rect.y -= 4
        elif keys[pygame.K_DOWN]:
            self.rect.y += 4
    def blit(self,surface):
        surface.blit(self.bullet, self.bullet_rect)
    def shoot(self):
        self.bullet_rect.y-=8
        if self.bullet_rect.y < 0:
            self.bullet_rect.midbottom=self.rect.midtop   
    def blit_health_indicator(self, surface):
        surface.blit(self.health_indicator2, self.health_indicator2_rect)
        surface.blit(self.health_indicator1, self.health_indicator1_rect)
    def health_indicator(self):
        self.health_indicator2_rect.midtop=self.rect.midbottom
        self.health_indicator1_rect.midtop=self.rect.midbottom
    def game_over(self):
        if self.width1<=0:
            screen.blit(self.game_over_text, self.game_over_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            exit()
    def player_y_x_limit(self):
        if self.rect.y<=200:
            self.rect.y=200
        elif self.rect.y>=490:
            self.rect.y=490
        elif self.rect.x>=705:
            self.rect.x=705
        elif self.rect.x<=10:
            self.rect.x=10
    def update(self):
        self.move()
        self.blit(screen)
        self.shoot()   
        self.blit_health_indicator(screen)
        self.health_indicator()
        self.game_over()
        self.player_y_x_limit()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader blue enemy.xcf")
        self.rect=self.image.get_rect(midbottom=(450,-5))
        self.image2=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader enemy yellow.xcf")
        self.rect2=self.image2.get_rect(midbottom=(350,-5))
        self.image3=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader enemy pink.xcf")
        self.rect3=self.image3.get_rect(midbottom=(250,-5))
        self.game_over_font = pygame.font.SysFont("Arial", 100)
        self.game_over_text = self.game_over_font.render("Game Over", True, (255, 255,255))
        self.game_over_rect = self.game_over_text.get_rect(center=(400, 300))
        self.lives=5
        self.lives_font= pygame.font.SysFont("Arial", 50)
        self.lives_text = self.lives_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.lives_rect = self.lives_text.get_rect(topleft=(5, 10))
        self.score=0
        self.score_font=pygame.font.SysFont("Arial",50)
        self.score_text=self.score_font.render(f"Score:{self.score}",True,(255,255,255))
        self.score_rect=self.score_text.get_rect(topleft=(4,75))
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
        global score,score_rect,score_text,score_font,spawn_rate
        if player.bullet_rect.colliderect(self.rect): 
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect.y=800          
            score+=20
            score_text=score_font.render(f"Score:{score}",True,(255,255,255))
            score_rect=score_text.get_rect(topleft=(4,75))
            spawn_rate-=20
            pygame.time.set_timer(Userevent, spawn_rate)  
        elif player.bullet_rect.colliderect(self.rect2):
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect2.y=800
            score+=20
            score_text=score_font.render(f"Score:{score}",True,(255,255,255))
            score_rect=score_text.get_rect(topleft=(4,75))
            spawn_rate-=20
            pygame.time.set_timer(Userevent, spawn_rate)  
        elif player.bullet_rect.colliderect(self.rect3):
            player.bullet_rect.midbottom = player.rect.midtop
            self.rect3.y=800
            score+=20
            score_text=score_font.render(f"Score:{score}",True,(255,255,255))
            score_rect=score_text.get_rect(topleft=(4,75))
            spawn_rate-=20
            pygame.time.set_timer(Userevent, spawn_rate)  
    def health_indicator_low(self,player):
        if player.rect.colliderect(self.rect):
            player.width1-=0.3   
            player.health_indicator1 = pygame.Surface((player.width1, 15))
            player.health_indicator1.fill((0, 255, 0))
        if player.rect.colliderect(self.rect2):
            player.width1-=0.3
            player.health_indicator1 = pygame.Surface((player.width1, 15))
            player.health_indicator1.fill((0, 255, 0))
        if player.rect.colliderect(self.rect3):
            player.width1-=0.3
            player.health_indicator1 = pygame.Surface((player.width1, 15))
            player.health_indicator1.fill((0, 255, 0))
    def game_over2(self):
        global lives,lives_text,lives_rect
        if self.rect.y == 600 or self.rect2.y == 600 or self.rect3.y == 600:
            lives -= 1
            lives_text = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
            lives_rect = lives_text.get_rect(topleft=(5, 10))
        elif lives <= 0:
            screen.blit(self.game_over_text, self.game_over_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            exit()
    def game_won(self):
        global spawn_rate
        if spawn_rate==1400:
            spawn_rate=1400
    def update(self):
        self.move()
        self.blit(screen)
        self.kill1()
        self.shoot_enemy(player_group.sprite)
        self.health_indicator_low(player_group.sprite)
        self.game_over2()
        self.game_won()
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
background=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invaders background.jpg").convert_alpha()
player=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader player ship.xcf").convert_alpha()
player_rect=player.get_rect(midbottom=(400,555))
enemy_blue=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader blue enemy.xcf").convert_alpha()
enemy_pink=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader enemy pink.xcf").convert_alpha()
enemy_yellow=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\space invader enemy yellow.xcf").convert_alpha()
bullet=pygame.Surface((10, 20))
bullet.fill((255, 0, 0))
bullet_rect=bullet.get_rect(midbottom=(400,555))
# Health indicators
width1=100
width2=100
health_indicator1=pygame.Surface((width1,15))
health_indicator1.fill((0, 255, 0))
health_indicator1_rect=health_indicator1.get_rect(topleft=(10, 10))
health_indicator2=pygame.Surface((width2,15))
health_indicator2.fill((255,0,0))
health_indicator2_rect=health_indicator2.get_rect(topleft=(40, 10))
# Game_over_screen
game_over_font = pygame.font.SysFont("Arial", 100)
game_over_text = game_over_font.render("Game Over", True, (255, 255,255))
game_over_rect = game_over_text.get_rect(center=(400, 300))
lives=5
lives_font= pygame.font.SysFont("Arial", 50)
lives_text = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
lives_rect = lives_text.get_rect(topleft=(5, 10))
score=0
score_font=pygame.font.SysFont("Arial",50)
score_text=score_font.render(f"Score:{score}",True,(255,255,255))
score_rect=score_text.get_rect(topleft=(4,75))
clock=pygame.time.Clock()
Userevent = pygame.USEREVENT + 1
spawn_rate=3000
pygame.time.set_timer(Userevent, spawn_rate)  
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
    screen.blit(lives_text, lives_rect)
    screen.blit(score_text,score_rect)
    pygame.display.update()
    clock.tick(60)