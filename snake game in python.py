import pygame
from sys import exit
import random
def game_overscreen():
     global score3,text2,text3
     if game_reset==False:
          screen.blit(background,(0,0))
          score3=f'Your Score is:{score1}'
          font2=pygame.font.SysFont('Arial',50)
          text2=font2.render(score3,True,(255,255,255))
          screen.blit(text2,(170,200))
          font3=pygame.font.SysFont('Arial',40)
          text3=font3.render("Press Space To Play Again",True,(255,255,255))
          screen.blit(text3,(150,275))
pygame.init()
cell_size=20
cell_no=30
screen=pygame.display.set_mode((cell_size*cell_no,cell_size*cell_no))
pygame.display.set_caption("Snake Game")
background=pygame.image.load("C:\\Users\\Ansh\\Desktop\\images_game\\snake game background.jpg")
snake_colour=(0,255,0)
snake_surf=pygame.Surface((cell_size,cell_size))
snake_colour_fill=snake_surf.fill(snake_colour)
snake_pos=[(5,5)]
snake_direction=(1,0)
snake_head=snake_pos[0]
snake_rect=snake_surf.get_rect(center=(snake_head))
food=pygame.Surface((cell_size,cell_size))
food_green=(0,255,0)
food_red=(255,0,0)
food.fill(food_red)
food_rect=food.get_rect(center=(400,300))
score1=0
score2=f'{score1}'
score3=f'Your Score is:{score1}'
font1=pygame.font.SysFont('Arial',50)
text1=font1.render(score2,True,(255,255,255))
font2=pygame.font.SysFont('Arial',50)
text2=font2.render(score3,True,(255,255,255))
font3=pygame.font.SysFont('Arial',40)
text3=font3.render("Press Space To Play Again",True,(255,255,255))
Userevent=pygame.USEREVENT+1
pygame.time.set_timer(Userevent,200)
clock=pygame.time.Clock()
running=True
Userevent=pygame.USEREVENT+1
pygame.time.set_timer(Userevent,150)
Userevent2=pygame.USEREVENT+2
pygame.time.set_timer(Userevent2,1000)
game_reset=True
while running:   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
             pygame.quit()
             exit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)
                if event.key==pygame.K_SPACE and game_reset==False:
                     game_reset=True
                     del snake_pos[1:]
                     score1=0 
                     score2=f'{score1}'
                     font1=pygame.font.SysFont('Arial',50)
                     text1=font1.render(score2,True,(255,255,255)) 
                     screen.blit(text1,(287,10))
            if event.type==Userevent:
                global new_x,new_y
                head_x,head_y=snake_pos[0]
                new_x=(head_x+snake_direction[0])%cell_no
                new_y=(head_y+snake_direction[1])%cell_no           
                snake_pos.insert(0,(new_x,new_y))
                snake_rect = pygame.Rect(new_x * cell_size, new_y * cell_size, cell_size, cell_size)
                if food_rect.colliderect(snake_rect):
                            food_rect.x=random.randint(0,550)
                            food_rect.y=random.randint(0,550)
                            score1+=1
                            score2=f'{score1}'
                            # score3=f'Your Score is:{score1}'
                            text1=font1.render(score2,True,(255,255,255))          
                elif (new_x,new_y) in snake_pos[1:]:
                     game_reset=False               
                elif segment_rect.colliderect(snake_rect):
                     food_rect.x=random.randint(0,550)
                     food_rect.y=random.randint(0,550)            
                else:
                    snake_pos.pop()    
        screen.blit(background,(0,0))
        screen.blit(food,food_rect)
        screen.blit(text1,(287,10))
        for segment in snake_pos:
            segment_rect = pygame.Rect(segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size)
            screen.blit(snake_surf,segment_rect)      
        game_overscreen()
        pygame.display.update()
        clock.tick(60)