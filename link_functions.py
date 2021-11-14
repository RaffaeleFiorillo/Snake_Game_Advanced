import auxiliar_functions as af
import game_entities as ge
import movement_functions as mf
import menu_classes as mc


def main_menu(screen):
    buttons = []
    menu = mc.Menu(screen, buttons, "main_menu.png")
    menu.display_menu()


def game(screen, movement_type=mf.keyboard_movement):
    world = ge.World(screen, af.WORLD_SIZE, af.CELL_SIZE)
    snake_moving_function = movement_type  # setting the snake to move according to parameter
    while True:
        af.CLOCK.tick(15)
        world.snake_growth()
        snake_moving_function(world)
        world.refresh(af.TEXT_FONT)
        world.verify_death_condition()
