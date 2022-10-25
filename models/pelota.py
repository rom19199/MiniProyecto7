from settings import *

class Pelota(object):

    def __init__(self, x: int, y: int, game_positions: list, game_screen) -> None:
        self.x = x
        self.y = y
        self.game_positions = game_positions
        self.game_screen = game_screen
        self.paint_color = GREEN

    def draw_game(self) -> None:
        self.game_screen.set_at((self.x, self.y), GREEN)
        self.game_positions[self.x][self.y] = EMPTY

    def update_game(self) -> None:
        self.paint_color = self.game_screen.get_at((self.x, self.y))
        self.game_screen.set_at((self.x, self.y), RED)
        self.game_positions[self.x][self.y] = RED

    def move(self, x:int, y:int) -> None:
        self.draw_game()
        self.x += x
        self.y += y
        self.update_game()

    def get_position(self) -> tuple:
        return self.x, self.y
