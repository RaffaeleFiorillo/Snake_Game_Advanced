import pygame
import moving_functions as mf
import game_entities as ge

pygame.init()
pygame.font.init()
WORLD_SIZE = 24
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((WORLD_SIZE*CELL_SIZE, WORLD_SIZE*CELL_SIZE))
CLOCK = pygame.time.Clock()
TEXT_FONT = pygame.font.SysFont('Times New Roman', 12)


world = ge.World(SCREEN, WORLD_SIZE, CELL_SIZE)
# snake moving options: *x_movement* where x: keyboard, random, hamiltonian
snake_moving_function = mf.hamiltonian_movement_simplified  # setting the snake to move with keyboard
while True:
    CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    world.snake_growth()
    snake_moving_function(world)
    world.refresh(TEXT_FONT)
    world.verify_death_condition()
