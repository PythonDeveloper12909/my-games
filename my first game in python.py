
import pygame
from sys import exit
from random import randint,choice
class Player(pygame.sprite.Sprite):
       def __init__(self):
              super().__init__()
              self.image2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop2.xcf').convert_alpha()
              self.gravity=0
              self.character2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop.xcf').convert_alpha()
              self.character1=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop2.xcf').convert_alpha()
              self.character3=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop3.xcf').convert_alpha()
              self.character4=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop4.xcf').convert_alpha()
              self.character=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop2.xcf').convert_alpha()
              self.character_walk=[character1,character2,character3,character4]
              self.character_index=0
              self.character_surf=character_walk[character_index]
              self.image=self.character_walk[self.character_index]  
              self.rect=self.image.get_rect(midbottom=(100,470))
              self.sound=pygame.mixer.Sound('C:\\Users\\dell\\Desktop\\images_game\\jump sound.wav')
              self.sound.set_volume(1.0)
       def player_controll(self):
              keys=pygame.key.get_pressed()
              if keys[pygame.K_SPACE] and self.rect.bottom==470 and game_reset==True: 
                                                                self.gravity=-25
                                                                self.sound.play()
       def apply_gravity(self):
              self.gravity+=1
              self.rect.y+=self.gravity
              if self.rect.bottom>470:
                     self.rect.bottom=470
       def player_animation(self):   
              if self.rect.bottom<470:
                    self.image=self.character1
              else:
                    self.character_index+=0.1
                    if self.character_index>=len(self.character_walk): 
                                                    self.character_index=0   
                    self.image=self.character_walk[int(self.character_index)]
       
       
       def update(self):
              self.player_controll()
              self.apply_gravity()
              self.player_animation()
class Obstacles(pygame.sprite.Sprite):
        def __init__(self,type):
                super().__init__() 
                if type=='fly':
                        bird1=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop3.xcf').convert_alpha()
                        bird4=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop1.xcf').convert_alpha()
                        bird2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop2.xcf').convert_alpha()
                        bird3=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop4.xcf').convert_alpha()
                        self.frames=[bird1,bird2,bird3,bird4]
                        self.y_pos=350
                else:
                        snail2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\snail.xcf').convert_alpha()
                        snail=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\snail2.xcf').convert_alpha()
                        self.frames=[snail,snail2]
                        self.y_pos=470
                self.animation_index=0
                self.image=self.frames[self.animation_index]
                self.rect=self.image.get_rect(midbottom=(randint(900,1100),self.y_pos))
        def obstacles_animation(self):
                self.animation_index+=0.1
                if self.animation_index>=len(self.frames):
                        self.animation_index=0
                self.image=self.frames[int(self.animation_index)]
        def destroy(self):
                if self.rect.x<=-50:
                        self.kill()
        def update(self):
                self.obstacles_animation()
                self.rect.x-=5
                self.destroy()
                        
                        
              
       


pygame.init()
pygame.display.set_caption('Runner') 
def display():
    global score
    score=int(pygame.time.get_ticks()/1000)-start_time
    score_surf=font.render(f'Score:{score}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,100))
    screen.blit(score_surf,score_rect)
def func(obstacle_list1):
    if obstacle_list1:
        for a in obstacle_list1:
            a.x-=5
            if a.centery==350:
                        screen.blit(bird_surf,a)
            else:
                screen.blit(snail_surf,a)
        obstacle_list1=[a for a in obstacle_list1 if a.x >0]
        return obstacle_list1
    else:
        return []
def collisions(player,obstacles):
    if obstacles:
        for b in obstacles:
            if player.colliderect(b):
                return False
    return True
def character_animation():
        global character_surf,character_walk,character_rect,character_index
        if character_rect.bottom<470:
                character_surf=character1 
        else:
            character_index+=0.1
            if character_index>=len(character_walk):
                    character_index=0
            else:
                character_surf=character_walk[int(character_index)]
def collisions_sprite():
                if pygame.sprite.spritecollide(player.sprite,obstacle,False):
                                                                    obstacle.empty()
                                                                    return False
                else:
                        return True



score4=int(pygame.time.get_ticks()/1000)
screen = pygame.display.set_mode((800, 600))  
surface = pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\background2.png')
font=pygame.font.SysFont('Arial',55)
snail2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\snail.xcf').convert_alpha()
snail=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\snail2.xcf').convert_alpha()
snail_walk=[snail,snail2]
snail_index=0
snail_surf=snail_walk[snail_index]
character2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop.xcf').convert_alpha()
character1=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop2.xcf').convert_alpha()
character3=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop3.xcf').convert_alpha()
character4=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop4.xcf').convert_alpha()
character=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\characterop2.xcf').convert_alpha()
character_walk=[character1,character2,character3,character4]
character_index=0
character_surf=character_walk[character_index]
character_rect1=character.get_rect(center=(400,300))
character_scaled=pygame.transform.rotozoom(character,0,2)
character_rect_scaled=character_scaled.get_rect(center=(400,300))
character_rect=character.get_rect(midbottom=(100,470))
snail_rect2=snail.get_rect(midbottom=(800,480))
snail_rect2.left=800
bird1=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop1.xcf').convert_alpha()
bird2=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop2.xcf').convert_alpha()
bird3=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop3.xcf').convert_alpha()
bird4=pygame.image.load('C:\\Users\\dell\\Desktop\\images_game\\birdop4.xcf').convert_alpha()
bird_walk=[bird1,bird2,bird3,bird4]
bird_index=0
bird_surf=bird_walk[bird_index]
bird_rect=bird1.get_rect(center=(700,350)) 
start_time1=int(pygame.time.get_ticks()/1000)
start_time=0
game_reset=True
character_gravity=0
obstacle_list=[]
event_gen=pygame.USEREVENT + 1
pygame.time.set_timer(event_gen,5000)
clock=pygame.time.Clock()
event_snail_animation=pygame.USEREVENT + 2
pygame.time.set_timer(event_snail_animation,500)
event_bird_animation=pygame.USEREVENT + 3
pygame.time.set_timer(event_bird_animation,200)
player=pygame.sprite.GroupSingle()
player.add((Player()))
obstacle=pygame.sprite.Group()
backgroundsound=pygame.mixer.Sound('C:\\Users\\dell\\Desktop\\images_game\\background sound.wav')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()       
                exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
             if character_rect.collidepoint(event.pos) and character_rect.bottom==470:
                                                                character_gravity=-25 
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and character_rect.bottom==470:
                                            character_gravity=-25
        if event.type==pygame.KEYDOWN and game_reset==False:
            if event.key==pygame.K_s:
                game_reset=True
                snail_rect2.left=800
                start_time=int(pygame.time.get_ticks()/1000)
                start_time1=int(pygame.time.get_ticks()/1000)
        if event.type==pygame.KEYDOWN and game_reset==False:
            if event.key==pygame.K_z:
                pygame.quit()
                exit()

        if event.type==event_gen and game_reset:
            obstacle.add(Obstacles(choice(['fly','snail','snail','snail'])))                    
            # if randint(0,2)==0:  
            #             obstacle_list.append(snail_surf.get_rect(midbottom=(randint(800,1100),460)))
            # else:
            #     obstacle_list.append(bird_surf.get_rect(center=(randint(800,1000),350)))
        if event.type==event_snail_animation and game_reset:
            if snail_index==0:
                snail_index=1   
            else:
                snail_index=0
            snail_surf=snail_walk[snail_index]
        if event.type==event_bird_animation and game_reset:
               if bird_index==0:
                      bird_index=1
               elif bird_index==1:
                      bird_index=2
               elif bird_index==2:
                      bird_index=3
               elif bird_index==3:
                      bird_index=1
               bird_surf=bird_walk[bird_index]
    
    if game_reset:

        screen.blit(surface,(0,0))
        display()
        # func(obstacle_list)
        # screen.blit(snail,snail_rect)
        
        # screen.blit(character_surf,character_rect)
        mouse_pos=pygame.mouse.get_pos()
        # if not snail_rect.left in range(0,800+1):
        #                         snail_rect.left=800
        player.draw(screen)
        player.update()
        obstacle.draw(screen)
        obstacle.update()
        
        # character_animation()
        # screen.blit(bird,bird_rect)
        # character_gravity+=1
        # character_rect.y+=character_gravity
        # if character_rect.bottom > 470:
        #             character_rect.bottom = 470
                    
        # # if character_rect.colliderect(snail_rect):
        # #                         game_reset=False
        game_reset=collisions_sprite()
        backgroundsound.play(loops=-1)
        backgroundsound.set_volume(0.3)
    else:
        screen.fill((230,230,230))
        screen.blit(character_scaled,character_rect_scaled)
        font1=pygame.font.SysFont('Arial',25)
        text1=font1.render('do u want to restart if yes, please press "s" key,if "no",please press "z"',False,(11,34,200))
        font2=pygame.font.SysFont('Arial',50)
        text2=font2.render('Mario Game',False,(54,23,155))
        score2=pygame.font.SysFont('Arial',50)
        score3=score2.render(f'Final Score:{score}',False,(54,24,156))
        screen.blit(score3,(250,450))        
        screen.blit(text1,(1,400))
        screen.blit(text2,(250,100))
        obstacle_list.clear()
        character_rect.midbottom = (100,480)
        character_gravity = 0
        backgroundsound.stop()
    pygame.display.update()
    # snail_rect.right-=5   
    clock.tick(30)
