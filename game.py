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
import math
from difuse import *


def drawVertLine(x1, x2, y, game):
    for x in range(x1, x2):
        game[x][y] = SCORE


def drawHorLine(y1, y2, x, game):
    for y in range(y1, y2):
        game[x][y] = SCORE


def game():
    juego = [[EMPTY for _ in range(SCREEN)] for _ in range(SCREEN)]

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
                jugador = Jugador(x, y, juego, pantalla)
                pantalla.set_at((x, y), BLACK)
            elif juego[x][y] == PELOTA:
                pelota = Pelota(x, y, juego, pantalla)
                pantalla.set_at((x, y), RED)

    contenedor.blit(pygame.transform.scale(
        pantalla, contenedor.get_rect().size), (0, 0))

    movimiento_velocidad = 0
    movimiento_fuerza = 0

    try:
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pelota_x, pelota_y = pelota.get_position()
            jugador_x, jugador_y = jugador.get_position()

            distancia = math.sqrt(abs(pelota_x - jugador_x) **
                                2 + abs(pelota_y - jugador_y)**2)

            if distancia < 2:
                fuerza_sim.input['velocidad_jugador'] = movimiento_velocidad
                fuerza_sim.input['distancia_porteria'] = math.sqrt(abs(pelota_x - 99)**2 + abs(pelota_y - 50)**2)
                fuerza_sim.compute()

                movimiento_fuerza = fuerza_sim.output['fuerza_patada_afuera']
                cantidad_movimiento = math.sqrt(movimiento_fuerza**2 / 2)

                pelota_x_m = math.ceil(pelota_x + cantidad_movimiento)

                if pelota_x > 50:
                    pelota_y_m = math.ceil(pelota_y + cantidad_movimiento)
                    pelota.move(pelota_x_m, pelota_y_m)
                else:
                    pelota_y_m = math.ceil(pelota_y - cantidad_movimiento)
                    pelota.move(pelota_x_m, pelota_y_m)
            else:
                velocidad_sim.input['distancia_pelota'] = distancia
                velocidad_sim.input['posicion_relativa'] = pelota_x - jugador_x
                velocidad_sim.compute()

                movimiento_velocidad = velocidad_sim.output['velocidad_pelota_afuera']
                cantidad_movimiento = math.sqrt(movimiento_velocidad**2 / 2)

                m_x = cantidad_movimiento
                m_y = cantidad_movimiento

                m_x = abs(jugador_x - pelota_x) - 1 if m_x >= abs(jugador_x - pelota_x) else m_x
                m_y = abs(jugador_y - pelota_y) - 1 if m_y >= abs(jugador_y - pelota_y) else m_y

                if pelota_x < jugador_x:
                    jugador.move_left(int(m_x))
                elif pelota_x > jugador_x:
                    jugador.move_right(int(m_x))

                if pelota_y < jugador_y:
                    jugador.move_straight(int(m_y))
                elif pelota_y > jugador_y:
                    jugador.move_down(int(m_y))

            pygame.time.delay(150)
            pygame.display.update()
            contenedor.blit(pygame.transform.scale(
                pantalla, contenedor.get_rect().size), (0, 0))

    except:
        pygame.quit()
        quit()
