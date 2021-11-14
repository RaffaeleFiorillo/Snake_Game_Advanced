import pygame
from random import randint


class Snake:
    def __init__(self):
        self.body_coordinates = [(1, 0), (0, 0)]
        self.should_grow = False

    def move(self, vector):
        head_coo = [(self.body_coordinates[0][0] + vector[0], self.body_coordinates[0][1] + vector[1])]
        self.body_coordinates = [coo for coo in self.body_coordinates[:-1]]
        self.body_coordinates = head_coo + self.body_coordinates


class Food:
    def __init__(self, snake_body_coo, world_size):
        self.coordinates = (randint(0, world_size-1), randint(0, world_size-1))
        while self.coordinates in snake_body_coo and len(snake_body_coo) != world_size**2:
            self.coordinates = (randint(0, world_size-1), randint(0, world_size-1))


class World:
    def __init__(self, screen, w_size, c_size):
        self.screen = screen
        self.last_vector = (1, 0)
        self.size = w_size
        self.cell_size = c_size
        self.SNAKE = Snake()
        self.FOOD = Food(self.SNAKE.body_coordinates, self.size)
        self.make_snake_grow, self.last_food_coo = False, []

    def move_snake(self, key=False):
        if key:
            key_effects = {pygame.K_RIGHT: (1, 0), pygame.K_LEFT: (-1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}
            self.last_vector = key_effects[key]
        self.SNAKE.move(self.last_vector)
        """# after the snake moves, the cell where the head of the snake used to be must be drawn again
        # it is a better alternative to always draw all of the squares in the snake body: From: O(n**2) To: O(k);
        x_coo = self.cell_size * self.SNAKE.body_coordinates[1][0]
        y_coo = self.cell_size * self.SNAKE.body_coordinates[1][1]
        pygame.draw.rect(self.screen, (0, 255, 0), (x_coo, y_coo, self.cell_size-2, self.cell_size-2), self.cell_size//10)
        # after the snake moves, the cell where the last bit of the snake used to be must be changed to black again
        # it is a better alternative to always draw all of the squares in the cell-grid: From: O(n**2) To: O(k);
        x_size = self.cell_size * self.SNAKE.body_coordinates[-1][0]
        y_size = self.cell_size * self.SNAKE.body_coordinates[-1][1]
        pygame.draw.rect(self.screen, (0, 0, 0), (x_size, y_size, self.cell_size, self.cell_size))"""

    def snake_growth(self):
        if self.SNAKE.should_grow:
            self.last_food_coo.append(self.FOOD.coordinates)
            self.FOOD = Food(self.SNAKE.body_coordinates, self.size)
            self.SNAKE.should_grow = False
        if self.last_food_coo and self.SNAKE.body_coordinates[-1] in self.last_food_coo:
            new_body_coo = self.last_food_coo.index(self.SNAKE.body_coordinates[-1])
            self.SNAKE.body_coordinates.append(new_body_coo)
            self.last_food_coo.pop(new_body_coo)

    def verify_death_condition(self):
        for coo in self.SNAKE.body_coordinates[1:]:
            if self.SNAKE.body_coordinates[0] == coo:
                self.draw_world_entity(self.SNAKE.body_coordinates[0], (255, 0, 0))  # drawing the head of the snake
                pygame.display.update()
                pygame.time.wait(200)
                exit()

    def adjust_snake_position(self):
        self.SNAKE.body_coordinates[0] = (self.SNAKE.body_coordinates[0][0] % self.size,
                                          self.SNAKE.body_coordinates[0][1] % self.size)
        if self.SNAKE.body_coordinates[0] == self.FOOD.coordinates:
            self.SNAKE.should_grow = True

    def draw_world_entity(self, entity_coo: (int, int), color: (int, int, int)) -> None:
        entity_rect = (self.cell_size * entity_coo[0], self.cell_size * entity_coo[1], self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, entity_rect)  # (0, 200, 200)

    def refresh(self, text_font: pygame.font.Font):
        self.adjust_snake_position()
        self.draw()
        self.screen.blit(text_font.render(str(len(self.SNAKE.body_coordinates)), True, (255, 0, 0)), (5, 3))
        pygame.display.update()

    def draw(self):
        [pygame.draw.rect(self.screen, (0, 0, 0), (self.cell_size*i, self.cell_size*y, self.cell_size, self.cell_size))
         for y in range(self.size) for i in range(self.size)]
        self.draw_world_entity(self.SNAKE.body_coordinates[0], (0, 200, 200))  # drawing the head of the snake
        [pygame.draw.rect(self.screen, (0, 255, 0),
                          (self.cell_size*i, self.cell_size*y, self.cell_size, self.cell_size), int(self.cell_size*0.1))
         for i, y in self.SNAKE.body_coordinates[1:]]
        self.draw_world_entity(self.FOOD.coordinates, (255, 255, 0))  # drawing the food
