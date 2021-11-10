import pygame
import movement_functions as mf
import game_entities as ge

pygame.init()
pygame.font.init()
WORLD_SIZE = 20
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((WORLD_SIZE*CELL_SIZE, WORLD_SIZE*CELL_SIZE))
CLOCK = pygame.time.Clock()
TEXT_FONT = pygame.font.SysFont('Times New Roman', 12)


world = ge.World(SCREEN, WORLD_SIZE, CELL_SIZE)
# snake moving options: *x_movement* where x: keyboard, random, hamiltonian
snake_moving_function = mf.keyboard_movement  # setting the snake to move with keyboard
while True:
    CLOCK.tick(15)
    world.snake_growth()
    snake_moving_function(world)
    world.refresh(TEXT_FONT)
    world.verify_death_condition()
