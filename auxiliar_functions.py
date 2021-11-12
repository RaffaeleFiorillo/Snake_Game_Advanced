import pygame

pygame.font.init()

WORLD_SIZE = 20
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((WORLD_SIZE * CELL_SIZE, WORLD_SIZE * CELL_SIZE))
CLOCK = pygame.time.Clock()
TEXT_FONT = pygame.font.SysFont('Times New Roman', 12)


# returns an image ready to be displayed on the screen. "convert_alpha" makes it much faster to display
def load_image(directory: str)-> pygame.Surface:
    return pygame.image.load(f"images/{directory}").convert_alpha()


class Game:
    link_function_dict: dict

    def __init__(self, screen_lable, link_functions):
        self.screen = None
        self.link_function_dict = link_functions
        self.previous_link = None
        self.create_screen(screen_lable)

    def create_screen(self, lable: str) -> None:
        global SCREEN
        pygame.display.set_caption(lable)
        self.screen = SCREEN  # module must be initialized or the "convert_alpha" method wont work

    def start(self, link: str, state=True) -> None:
        keys_list = list(self.link_function_dict.keys())
        while True:
            if state:
                self.previous_link = keys_list[keys_list.index(link)]  # saving current link in case the state is False
                state = self.link_function_dict[link](self.screen)
                if state:
                    link = state
                    state = True
            else:  # In case the user wants to exit the game by clicking on the red crux the state is set to False
                state = self.link_function_dict["exit1"](self.screen)
                link = self.previous_link
