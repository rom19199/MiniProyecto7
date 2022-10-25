import skfuzzy as skf
from skfuzzy import control as ctrl
import numpy as np

# Create universe variables
distancia_pelota = ctrl.Antecedent(np.arange(0, 142, 1), 'distancia_pelota')
posicion_relativa = ctrl.Antecedent(np.arange(-100, 100, 1), 'posicion_relativa')
velocidad_pelota_afuera = ctrl.Consequent(np.arange(1, 20, 1), 'velocidad_pelota_afuera')

# Patada
velocidad_jugador = ctrl.Antecedent(np.arange(5, 20, 5), 'velocidad_jugador')
distancia_porteria = ctrl.Antecedent(np.arange(0, 142, 1), 'distancia_porteria')
fuerza_patada_afuera = ctrl.Consequent(np.arange(1, 10, 1), 'fuerza_patada_afuera')

distancia_pelota['near'] = skf.trimf(distancia_pelota.universe, [0, 0, 103])
distancia_pelota['far'] = skf.trimf(distancia_pelota.universe, [39, 142, 142])

posicion_relativa.automf(3)
velocidad_pelota_afuera.automf(3)
velocidad_jugador.automf(3)

distancia_porteria['near'] = skf.trimf(distancia_porteria.universe, [0, 0, 103])
distancia_porteria['far'] = skf.trimf(distancia_porteria.universe, [39, 142, 142])

fuerza_patada_afuera.automf(3)

# Distancia reglas del juego

regla1 = ctrl.Rule((posicion_relativa['good'] & distancia_pelota['near']) | (posicion_relativa['average'] & distancia_pelota['far']), velocidad_pelota_afuera['poor'])

regla2 = ctrl.Rule((posicion_relativa['average'] & distancia_pelota['near']) | (posicion_relativa['good'] & distancia_pelota['far']), velocidad_pelota_afuera['average'])

regla3 = ctrl.Rule((distancia_pelota['far'] | distancia_pelota['near']) & posicion_relativa['poor'], velocidad_pelota_afuera['average'])

regla4 = ctrl.Rule((velocidad_jugador['good'] & distancia_porteria['far']) | (velocidad_jugador['average'] & distancia_porteria['near']), fuerza_patada_afuera['poor'])

regla5 = ctrl.Rule((velocidad_jugador['average'] & distancia_porteria['near']), fuerza_patada_afuera['average'])

regla6 = ctrl.Rule((velocidad_jugador['average'] & distancia_porteria['far']) | (velocidad_jugador['good'] & distancia_porteria['near']), fuerza_patada_afuera['average'])


# controles
velocidad = ctrl.ControlSystem([regla1, regla2, regla3])
fuerza = ctrl.ControlSystem([regla4, regla5, regla6])

# simulacion
velocidad_sim = ctrl.ControlSystemSimulation(velocidad)
fuerza_sim = ctrl.ControlSystemSimulation(fuerza)
