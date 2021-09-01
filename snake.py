import pygame, random
from pygame.locals import *

pygame.init()
#Tamanho da tela
screen = pygame.display.set_mode((600,600))
#Titulo
pygame.display.set_caption('Snake')

while True:
    #Pegar os eventos que forem feito dentro do jogo
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()

    pygame.display.update()

