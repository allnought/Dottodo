import pygame
from pygame.locals import  *
import random
from random import *
import os
import sys
import pygame.freetype


width, height = 900, 500

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.flip()

background = pygame.image.load("data/back_sprite.png")
sprite_good = pygame.image.load("data/good.png")
sprite_obstacle = pygame.image.load("data/obstacle.png")


pygame.init()
pygame.mixer.init()

good1 = pygame.mixer.Sound("data/good1.wav")
good2 = pygame.mixer.Sound("data/good2.wav")
good3 = pygame.mixer.Sound("data/good3.wav")
good4 = pygame.mixer.Sound("data/good4.wav")
good5 = pygame.mixer.Sound("data/good5.wav")
dead = pygame.mixer.Sound("data/dead.wav")

pygame.mixer.Sound.set_volume(good1, 0.2)
pygame.mixer.Sound.set_volume(good2, 0.2)
pygame.mixer.Sound.set_volume(good3, 0.2)
pygame.mixer.Sound.set_volume(good4, 0.2)
pygame.mixer.Sound.set_volume(good5, 0.2)


pygame.mixer.music.load('data/musek.wav')
pygame.mixer.music.play(-1)

pygame.display.set_caption("Dottodo")

based_score = 0

right = pygame.font.Font("data/Righteous-Regular.ttf", 25)

score_val = 0

text_surface = right.render('Score: 0', False, (0, 0, 0))
score_msg = "Score" + str(score_val)


FPS = 60
clock = pygame.time.Clock()


running = True

mouse_x, mouse_y = pygame.mouse.get_pos()

mouse_rect = Rect(mouse_x-25, mouse_y-25, 50, 50)


obstacles = []

good_x = randint(100, width-100)
good_y = randint(100, height-100)
good = Rect(good_x, good_y, 50, 50)




def run():
    score_msg = "Score" + str(score_val)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if good.collidepoint(mouse_x, mouse_y):
        spawn_obstacle()
        good_collect()
        good_sound()
        update_score()
    for obstacle in obstacles:
        if obstacle.collidepoint(mouse_x, mouse_y):
            death()
        if obstacle.colliderect(good):
            good_collect()
    mouse_rect.update(mouse_x-25, mouse_y-25, 50, 50) 
        
        
def death():
    global score_val
    obstacles.clear()
    score_val = 0
    good_collect()
    pygame.mixer.find_channel().play(dead)


def good_sound():
    sound_play = randint(1, 5)
    if sound_play == 1:
        pygame.mixer.find_channel().play(good1)
    if sound_play == 2:
        pygame.mixer.find_channel().play(good2)
    if sound_play == 3:
        pygame.mixer.find_channel().play(good3)
    if sound_play == 4:
        pygame.mixer.find_channel().play(good4)
    if sound_play == 5:
        pygame.mixer.find_channel().play(good5)


def update_score():
    global score_val
    score_val += 1
    print(score_val)
    text_surface = right.render(score_msg, False, (0, 0, 0))



def spawn_obstacle():
    obstacle_x = randint(0, width)
    obstacle_y = randint(0, height)
    obstacle = pygame.Rect(obstacle_x, obstacle_y, 50, 50)
    if not obstacle.colliderect(mouse_rect):
        obstacles.append(obstacle)
    else:
        spawn_obstacle()
    

def good_collect():
    good_x = randint(100, width-100)
    good_y = randint(100, height-100)
    good.update(good_x, good_y, 50, 50)
    if good.colliderect(mouse_rect):
        good_collect()


def draw_score():
    scoretext = right.render("Score {0}".format(score_val), 1, (0,0,0))
    screen.blit(scoretext, (5, 10))




def draw():
    screen.blit(background, (0, 0))
    for obstacle in obstacles:
        screen.blit(sprite_obstacle, obstacle)
    screen.blit(sprite_good, good)
    draw_score()
    pygame.display.flip()



while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
    run()
    draw()
