# Consideraciones
#   - La posicion de la pelota siempre sera conocida
#   - La posicion de la porteria siempre sera conocida
#   - La posicion del robot siempresera conocida
#   - Definir sistema de logica difusa para encontrar pelota
#   - Definir sistema de logica para saber la fuerza para patear la pelota

import pygame
from settings import *
from models.jugador import Jugador
from models.pelota import Pelota

def drawVertLine(x1, x2, y, game):
    for x in range(x1, x2):
        game[x][y] = SCORE

def drawHorLine(y1, y2, x, game):
    for y in range(y1, y2):
        game[x][y] = SCORE


def main():
    juego = [[EMPTY for _ in range(SCREEN)]  for _ in range(SCREEN)]

    xw = 10
    lh = 20

    gh = 50
    gc = int(SCREEN/2 - gh/2)

    drawHorLine(SCREEN-xw, SCREEN, lh, juego)
    drawHorLine(SCREEN-xw, SCREEN, SCREEN-lh, juego)
    drawVertLine(lh, SCREEN-lh, SCREEN-xw, juego)

    drawVertLine(gc, gc+gh, SCREEN-2, juego)
    drawVertLine(gc, gc+gh, SCREEN-1, juego)

    jugadorX = 2
    juegoCentro = int(SCREEN/2)
    juego[jugadorX][juegoCentro] = JUGADOR
    juego[jugadorX+10][juegoCentro] = PELOTA

    pygame.init()

    contenedor = pygame.display.set_mode((SCREEN*SCALE, SCREEN*SCALE))
    pantalla = pygame.Surface((SCREEN, SCREEN))

    for x in range(len(juego)):
        for y in range(len(juego[x])):
            if juego[x][y] == EMPTY:
                pantalla.set_at((x, y), GREEN)
            elif juego[x][y] == SCORE:
                pantalla.set_at((x, y), WHITE)
            elif juego[x][y] == JUGADOR:
                jugador = Jugador(
                    x,
                    y,
                    juego,
                    pantalla
                )
                pantalla.set_at((x, y), BLACK)
            elif juego[x][y] == PELOTA:
                pelota = Pelota(
                    x,
                    y,
                    juego,
                    pantalla
                )
                pantalla.set_at((x, y), RED)

    contenedor.blit(pygame.transform.scale(pantalla, contenedor.get_rect().size), (0, 0))
            

    velocidad = 0
    fuerza = 0

if __name__ == '__main__':
    main()
