#--------------
# IMPORTACIÓN DE LIBRERIAS
#--------------

import sensor
import time
import pyb
from machine import LED, Pin

# Declaración de variables para cámara

THRESHOLD = (100, 200)  # Umbral de escala de grsis para objetos oscuros
BINARY_VISIBLE = True  # Paso binario primero para ver en qué se está ejecutando la regresión lineal.

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA)  
sensor.skip_frames(time=2000) 
clock = time.clock()  

while True:
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD]) if BINARY_VISIBLE else sensor.snapshot() #Activación de la cámara con la activación condicionada del filtro binario.

    # Devuelve un objeto de línea similar a los objetos de línea devueltos por find_lines() y
    # find_line_segments(). Tienes x1(), y1(), x2(), y2(), length(),
    # theta() (rotación en grados), rho(), y magnitude().
    #
    # magnitud () representa lo bien que la regresión lineal funcionó. Significa algo
    # diferente para la regresión lineal robusta. En general, cuanto mayor sea el valor de la
    # mejor.

    #La variable Line conserva la información de la regresión lineal
    line = img.get_regression(
        [(255, 255) if BINARY_VISIBLE else THRESHOLD], robust=True
    )

    if line:
        img.draw_line(line.line(), color=127)
        if line:
            print(line) #Imprime los valores de la línea obtenida.
        else: "N/A"

    """if line: #Clasifica las líneas según su ángulo, debes modificarlo dependiendo de la línea que 
        if line.rho() > 0 and line.theta() <= 0:
            print("Linea recta")

        if line.rho() <= 0 and (line.theta() > 120):
            print("Curva")"""
