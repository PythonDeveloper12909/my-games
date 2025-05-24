import pygame
from sys import exit
import random
import time
def surface_groundorfloor_touch():
    if surface1_rect.y<=0:
        surface1_rect.y=0
    elif surface1_rect.y>=500:
        surface1_rect.y=500
    if surface2_rect.y<=0:
        surface2_rect.y=0
    elif surface2_rect.y>=500:
        surface2_rect.y=500
def ball_groundorfloor_touch():
    if ball_rect.y<=0:
        ball_rect.y=0
    elif ball_rect.y>=575:
        ball_rect.y=575
def ball_surface_touch():
    global ball_direction_x,ball_direction_y
    if ball_direction_x==1 and ball_rect.y==575:
        ball_direction_y=-1
        ball_direction_x=1
    elif ball_direction_x==1 and ball_rect.y==0:
        ball_direction_y=1
        ball_direction_x=1
    elif ball_direction_x==-1 and ball_rect.y==575:
        ball_direction_y=-1
        ball_direction_x=-1
    elif ball_direction_x==-1 and ball_rect.y==0:
        ball_direction_y=1
        ball_direction_x=-1
    elif ball_rect.colliderect(surface1_rect) and ball_direction_y==1:
        ball_direction_y=1
        ball_direction_x=1
    elif ball_rect.colliderect(surface1_rect) and ball_direction_y==-1:
        ball_direction_y=-1
        ball_direction_x=1
    elif ball_rect.colliderect(surface2_rect) and ball_direction_y==-1:
        ball_direction_y=-1
        ball_direction_x=-1
    elif ball_rect.colliderect(surface2_rect) and ball_direction_y==1:
        ball_direction_y=1
        ball_direction_x=-1
def ball_reset():
    global ball_direction_x,ball_direction_y
    if ball_rect.x>=800:
        ball_rect.x=300
        ball_rect.y=200
        ball_direction_x=random.choice([-1,1])
        ball_direction_y=random.choice([-1,1])
    elif ball_rect.x<=0:
        ball_rect.x=300
        ball_rect.y=200
        ball_direction_x=random.choice([-1,1])
        ball_direction_y=random.choice([-1,1])
def opponent_ai():
    global direction
    if ball_rect.y>surface1_rect.y:
        direction=1
    elif ball_rect.y<surface1_rect.y:
        direction=-1
def score():
    global text,font,score1,text2,score2,font2
    if ball_rect.x==0:
        score1+=1
        font=pygame.font.SysFont('Arial',40)
        text=font.render(f'{score1}',True,(255,255,255))
    elif ball_rect.x==800:
        score2+=1
        font2=pygame.font.SysFont('Arial',40)
        text2=font2.render(f'{score2}',True,(255,255,255))
def game_over_screen():
    global game_reset1,game_reset2
    if score1==10:
        game_reset1=False 
    elif score2==10:
        game_reset2=False
def game_over_screen2():
    global game_reset_text,game_reset_font,game_reset_text_rect2,game_reset_text_rect3
    if game_reset2==False:
        screen.blit(background,(0,0))
        game_reset_font=pygame.font.SysFont('Arial',60)
        game_reset_text=game_reset_font.render("You Lost!",True,(255,0,0))
        screen.blit(game_reset_text,game_reset_text_rect)    
        game_reset_font2=pygame.font.SysFont('Arial',30)
        game_reset_text2=game_reset_font2.render('"Press Space To Play"',True,(255,0,0))
        screen.blit(game_reset_text2,game_reset_text_rect2)    
    elif game_reset1==False:
        screen.blit(background,(0,0))
        game_reset_font3=pygame.font.SysFont('Arial',60)
        game_reset_text3=game_reset_font3.render("You Won!",True,(0,255,0))
        game_reset_text_rect3=game_reset_text3.get_rect(center=(400,300))
        screen.blit(game_reset_text3,game_reset_text_rect3)
        game_reset_font4=pygame.font.SysFont('Arial',30)
        game_reset_text4=game_reset_font4.render('"Press Space To Play"',True,(0,255,0))
        game_reset_text_rect4=game_reset_text4.get_rect(center=(400,400))
        screen.blit(game_reset_text4,game_reset_text_rect4)
pygame.init()
screen=pygame.display.set_mode((800,600))
caption=pygame.display.set_caption("Ping Pong Game")
surface1=pygame.Surface((10,100))
surface1.fill((255,255,255))
surface1_rect=surface1.get_rect(topleft=(0,0))
surface2=pygame.Surface((10,100))
surface2.fill((255,255,255))
surface2_rect=surface2.get_rect(topright=(800,0))
background=pygame.image.load('C:\\Users\\Ansh\\Desktop\\images_game\\snake game background.jpg')
ball=pygame.Surface((25,25))
ball_rect=ball.get_rect(center=(400,300))
ball.fill((255,255,255))
score1=0
font=pygame.font.SysFont('Arial',40)
text=font.render(f'{score1}',True,(255,255,255))
text_rect=text.get_rect(center=(600,35))
score2=0
font2=pygame.font.SysFont('Arial',40)
text2=font2.render(f'{score2}',True,(255,255,255))
text_rect2=text2.get_rect(center=(200,35))
game_reset_font=pygame.font.SysFont('Arial',60)
game_reset_text=game_reset_font.render("You Lost!",True,(255,0,0))
game_reset_text_rect=game_reset_text.get_rect(center=(400,300))
game_reset_font2=pygame.font.SysFont('Arial',30)
game_reset_text2=game_reset_font2.render('"Press Space To Play"',True,(255,0,0))
game_reset_text_rect2=game_reset_text2.get_rect(center=(400,400))
game_reset_font3=pygame.font.SysFont('Arial',60)
game_reset_text3=game_reset_font3.render("You Won!",True,(0,255,0))
game_reset_text_rect3=game_reset_text3.get_rect(center=(400,300))
game_reset_font4=pygame.font.SysFont('Arial',30)
game_reset_text4=game_reset_font4.render('"Press Space To Play"',True,(0,255,0))
game_reset_text_rect4=game_reset_text4.get_rect(center=(400,400))
clock = pygame.time.Clock()
ball_speed=4
ball_direction_x=1
ball_direction_y=1
direction=1
speed=3.5
game_reset1=True
game_reset2=True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                surface2_rect.y += 30
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                surface2_rect.y-=30
        if event.type==pygame.KEYDOWN and game_reset2==False:
            if event.key==pygame.K_SPACE:
                game_reset2=True
                ball_rect.x=400
                ball_rect.y=300
                score1=0
                font=pygame.font.SysFont('Arial',40)
                text=font.render(f'{score1}',True,(255,255,255))
                text_rect=text.get_rect(center=(600,35))
                score2=0
                font2=pygame.font.SysFont('Arial',40)
                text2=font2.render(f'{score2}',True,(255,255,255))
                text_rect2=text2.get_rect(center=(200,35))
                surface2_rect.y=0
        if event.type==pygame.KEYDOWN and game_reset1==False:
            if event.key==pygame.K_SPACE:
                game_reset1=True
                ball_rect.x=400
                ball_rect.y=300
                score1=0
                font=pygame.font.SysFont('Arial',40)
                text=font.render(f'{score1}',True,(255,255,255))
                text_rect=text.get_rect(center=(600,35))
                score2=0
                font2=pygame.font.SysFont('Arial',40)
                text2=font2.render(f'{score2}',True,(255,255,255))
                text_rect2=text2.get_rect(center=(200,35))
                surface2_rect.y=0
    screen.blit(background,(0,0))
    pygame.draw.line(screen,(255,255,255),(400,0),(400,600),5)
    screen.blit(surface1,surface1_rect)
    screen.blit(surface2,surface2_rect)
    screen.blit(ball,ball_rect)
    screen.blit(text,text_rect)
    screen.blit(text2,text_rect2)
    ball_rect.x+=ball_speed*ball_direction_x
    ball_rect.y+=ball_speed*ball_direction_y
    surface1_rect.y+=speed*direction
    surface_groundorfloor_touch()
    ball_groundorfloor_touch()
    ball_surface_touch()
    opponent_ai()
    score()
    ball_reset()
    game_over_screen()
    game_over_screen2()
    pygame.display.update()
    clock.tick(60)