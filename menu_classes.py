import pygame
import auxiliar_functions as af


class Button:
    def __init__(self, x: int, y: int, directory: str, effect: str):
        self.x = x
        self.y = y
        if directory is not None:
            self.image = af.load_image(directory)
        self.effect = effect

    def cursor_is_inside(self, cursor_coo: (int, int)):
        cursor_x, cursor_y = cursor_coo[0], cursor_coo[1]
        button_width, button_height = self.image.get_size()[0], self.image.get_size()[1]
        if self.x <= cursor_x <= self.x + button_width and self.y <= cursor_y <= self.y + button_height:
            return True
        return False

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def change_image(self, directory: str):
        self.image = af.load_image(directory)


# provides a simple way of managing user input, both keyboard and mouse
class Basic_Input_Management:
    def __init__(self, buttons: [Button] = None):
        if buttons is None:
            buttons = []
        # self.button_activation_sound = button_y_sound
        self.clock = pygame.time.Clock()
        self.button_list = buttons
        self.active_code = 0
        self.coord_effect = None
        self.already_checked_cursor = False  # True means that actions have already been taken regarding cursor position

    def set_button_to_active(self, new_active_code: int):
        if new_active_code != self.active_code:
            # af.play(self.button_activation_sound)
            self.active_code = new_active_code
            self.coord_effect = self.update_coord_effect()

    def update_coord_effect(self):
        pass

    def manage_events(self):  # returns action to take based on input
        for event in pygame.event.Event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return self.get_effect_by_input(event)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.already_checked_cursor = True
                return self.get_effect_by_input()

    def manage_buttons(self, event: pygame.event.Event):
        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            return self.enter_action()

    def get_effect_by_input(self, event: pygame.event.Event = None):
        if event:  # if input is not None it means a key has been pressed
            effect = self.manage_buttons(event)
        else:
            effect = self.manage_mouse()
        return effect

    def cursor_is_on_button(self):
        mouse_position = pygame.mouse.get_pos()
        for button_index, button in enumerate(self.button_list):
            if button.cursor_is_inside(mouse_position):
                self.set_button_to_active(button_index)
                return True
        return False

    def enter_action(self):
        return self.button_list[self.active_code].effect

    def manage_mouse(self):
        if self.cursor_is_on_button():
            return self.enter_action()
        self.already_checked_cursor = False   # allows the cursor to interact with buttons again after the user clicks


class Menu(Basic_Input_Management):
    def __init__(self, screen: pygame.Surface, buttons: [Button], directory: str):
        super().__init__(buttons)
        self.directory = directory
        # self.name = self.directory.split("/")[-1][:-4]
        self.name_image = af.load_image(directory)
        self.user_related_images = []
        self.active_code = 0
        self.screen = screen
        self.coord_effect = self.update_coord_effect()

    def draw_buttons(self):
        for button in self.button_list:
            button.draw(self.screen)

    def update_coord_effect(self):
        return self.button_list[self.active_code].x, self.button_list[self.active_code].y

    def display_menu(self):
        while True:
            self.clock.tick(30)
            # effect carries information about what to do based on input. None is base case and means "do nothing"
            effect = self.manage_events()  # taking and evaluating input
            if effect is not None:  # if meaningful input is given take respective action
                return effect
            if not self.already_checked_cursor:  # saves time avoiding iterating over buttons when it was done already
                self.cursor_is_on_button()  # mouse visual interaction with interface
            self.refresh()

    def manage_buttons(self, event: pygame.event.Event):
        new_active_code = self.active_code  # go up if value is -1 and down if it's 1
        if event.key == pygame.K_UP:
            new_active_code -= 1
        elif event.key == pygame.K_DOWN:
            new_active_code += 1
        elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            return self.enter_action()
        new_active_code = new_active_code % len(self.button_list)  # make sure active_code doesn't go off-boundaries
        self.set_button_to_active(new_active_code)

    def refresh(self):
        self.draw_buttons()
        pygame.display.update()
