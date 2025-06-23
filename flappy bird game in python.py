import pygame 
from sys import exit
import random
class FlappyBird(pygame.sprite.Sprite):
     def __init__(self):
            super().__init__()
            # self.image=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\flappy bird new.xcf").convert_alpha()
            # self.rect=self.image.get_rect(center=(400,300))
            self.gravity=0
            self.animation_frame1=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame1.xcf").convert_alpha()
            self.animation_frame2=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame2.xcf").convert_alpha()
            self.animation_frame3=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame3.xcf").convert_alpha()
            self.bird_fly=[self.animation_frame1, self.animation_frame2, self.animation_frame3]
            self.bird_fly_index=0 
            self.image=self.bird_fly[self.bird_fly_index]
            self.rect=self.image.get_rect(center=(200,300))

     def gravity1(self):
            self.gravity+=0.1
            self.rect.y+=self.gravity
     def jump(self):
      self.gravity=-4        
     def collision(self):
           if self.rect.y>=570 or self.rect.y<=0:
                pygame.quit()
                exit()
     def animation(self):
           self.bird_fly_index+=0.1
           if self.bird_fly_index>=len(self.bird_fly):
                  self.bird_fly_index=0
           else:
                 self.image=self.bird_fly[int(self.bird_fly_index)]
     def update(self):
      self.gravity1()
      self.collision()
      self.animation()
class Pipe(pygame.sprite.Sprite):
     def __init__(self):
            super().__init__()
            self.image=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird pipe new.xcf").convert_alpha()
            self.image2=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird pipe2 new.xcf").convert_alpha()
            self.rect=self.image.get_rect(midtop=(900,400))
            self.rect2=self.image2.get_rect(midbottom=(900,200))
            self.obstacle_list=[self.rect, self.rect2]  
     def move(self):
            self.rect.x -= 2
            self.rect2.x -= 2
     def draw(self):
           screen.blit(self.image, self.rect)
           screen.blit(self.image2, self.rect2)
     def kill1(self):
           if self.rect.x < 0 and self.rect2.x < -100:
                self.kill()
     def collision(self):
                 if self.rect.colliderect(bird.rect) or self.rect2.colliderect(bird.rect):
                     pygame.quit()
                     exit()
     def update(self):
              self.move()
              self.draw()
              self.kill1()
              self.collision()
def infinte_pipespawn():
       pipe = Pipe()
       pipe_group.add(pipe)
       pipe.rect.y=random.choice([275, 250,275,275,410,450,300,400,400,380,300,250,235,235,235,410,410,450,450,450,450,475])
       pipe.rect2.y=pipe.rect.y-560   
def score():
      global score1, score_text, score_text_rect
      for pipe in pipe_group: 
       if bird.rect.x>=pipe.rect.x:
          if bird.rect.x==pipe.rect.x+1:
                     score1+=1
                     score_display=f'{score1}'
                     score_font=pygame.font.SysFont("Arial", 50)
                     score_text=score_font.render(score_display, True, (255, 255, 255))
                     score_text_rect=score_text.get_rect(center=(400, 50))
def remove_score():
      global score1, score_text, score_text_rect
      if bird.rect.x>=pipe.rect.x:
            if bird.rect.x==pipe.rect.x+1:
                        score1-=1
      
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
background=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird background.png").convert_alpha()
flappy_bird=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird new.xcf").convert_alpha()
flappy_bird_rect=flappy_bird.get_rect(center=(400,300))
pipe1=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird pipe new.xcf").convert_alpha()
pipe_inverted=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird pipe2 new.xcf").convert_alpha()
pipe_inverted_rect=pipe_inverted.get_rect(midbottom=(900,200))
pipe_rect=pipe1.get_rect(midtop=(900,350))
background_rect=background.get_rect(center=(400,300))
gravity=0
obstacle_list=[pipe_rect,pipe_inverted_rect]
clock=pygame.time.Clock()
userevent=pygame.USEREVENT+1
pygame.time.set_timer(userevent,4500)
bird=FlappyBird()
bird_group=pygame.sprite.GroupSingle()
bird_group.add(bird)
pipe=Pipe()
pipe2=Pipe()
pipe_group=pygame.sprite.Group()
pipe_group.add(pipe, pipe2)
score1=0
score_display=f'{score1}'
score_font=pygame.font.SysFont("Arial", 50)
score_text=score_font.render(score_display, True, (255, 255, 255))
score_text_rect=score_text.get_rect(center=(400, 50))
bird_animation1=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame1.xcf").convert_alpha()
bird_animation2=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame2.xcf").convert_alpha()
bird_animation3=pygame.image.load("C:\\Users\\dell\\Desktop\\images_game\\flappy bird animation frame3.xcf").convert_alpha()
bird_fly=[bird_animation1, bird_animation2, bird_animation3]
bird_fly_index=0
bird_surf=bird_fly[bird_fly_index]
bird_fly_animation=pygame.USEREVENT+2
pygame.time.set_timer(bird_fly_animation, 200)
while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    bird.jump()  
            if event.type==userevent:
                  infinte_pipespawn()
            if event.type==bird_fly_animation:
                  bird.animation()
        
        screen.blit(background, background_rect)
        # screen.blit(flappy_bird, flappy_bird_rect)
        # screen.blit(pipe, pipe_rect)
        # screen.blit(pipe_inverted, pipe_inverted_rect)
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
        pipe_group.update() 
        screen.blit(score_text, score_text_rect)  
        remove_score()
        score()
        pygame.display.update()
        clock.tick(60)