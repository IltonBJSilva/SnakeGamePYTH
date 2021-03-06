import pygame, random
from pygame.locals import *

pygame.init()
#Tamanho da tela
screen = pygame.display.set_mode((600,600))
#Titulo
pygame.display.set_caption('Snake')

#Direcoes
up = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Lista para a cobra, e uma tupla
snake = [(200, 200), (210, 200),(220,200)]
snake_skin = pygame.Surface((10,10))
#Cor da cobra
snake_skin.fill((255,255,255))

#Criacao da maca
apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))


#Vai iniciar indo para direita
my_direction = LEFT


while True:
    #Pegar os eventos que forem feito dentro do jogo
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()

    #Coloca cobra e macao na tela
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        #Gerar a cobra com uma tupla
        screen.blit(snake_skin,pos)

    pygame.display.update()