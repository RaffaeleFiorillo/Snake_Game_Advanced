import pygame
import auxiliar_functions as af
import link_functions as lf

pygame.init()
links = {False: exit, "main": lf.main_menu, "game": lf.game}

GAME = af.Game("Snake Game Advanced", links)
GAME.start("game")
