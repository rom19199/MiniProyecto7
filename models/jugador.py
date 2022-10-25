from settings import *

class Jugador(object):

    def __init__(self, x: int, y: int, game_positions: list, game_screen) -> None:
        self.x = x
        self.y = y
        self.game_positions = game_positions
        self.game_screen = game_screen

    def draw_game(self) -> None:
        self.game_screen.set_at((self.x, self.y), GREEN)
        self.game_positions[self.x][self.y] = EMPTY

    def update_game(self) -> None:
        self.game_screen.set_at((self.x, self.y), BLACK)
        self.game_positions[self.x][self.y] = BLACK

    def move_straight(self, scale: int = 1) -> None:
        self.draw_game()
        self.y -= scale
        self.update_game()

    def move_down(self, scale: int = 1) -> None:
        self.draw_game()
        self.y += scale
        self.update_game()

    def move_right(self, scale: int = 1) -> None:
        self.draw_game()
        self.x += scale
        self.update_game()

    def move_left(self, scale: int = 1) -> None:
        self.draw_game()
        self.x -= scale
        self.update_game()

    def get_position(self) -> tuple:
        return self.x, self.y
