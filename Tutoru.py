from ast import And 
from operator import and_
from tkinter import font
from turtle import Screen
import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    sceen.blit(score_surf,score_rect)
    print(current_time)

#Starting the item
pygame.init()
sceen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LazyBird')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Amatic-Bold.ttf', 51)
game_active = False
start_time = 0

# Elements
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('Hello Player', False, (64,64,64))
#score_rect = score_surface.get_rect(center = (400,50))

#Importing the players surface and collison system
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

#INTRO SCREEN
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400,200))

#THE ACTUAL GAME
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20   
            
            #JUMP 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
      
    if game_active:
        # Draw all the elements
        # Update everything
        # Ground surface is at 300,
        sceen.blit(ground_surface,(0,300))
        sceen.blit(sky_surface,(0,0))
#        pygame.draw.rect(sceen,'#c0e8ec',score_rect)
#        pygame.draw.rect(sceen,'#c0e8ec',score_rect,10)
#        sceen.blit(score_surface,score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        # Collisions with rectangles
        sceen.blit(snail_surface,snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        sceen.blit(player_surface,player_rect)


        #COLLISONS
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        sceen.fill((94,129,162))
        sceen.blit(player_stand,player_stand_rect)
    
    pygame.display.update()
    clock.tick(60)
