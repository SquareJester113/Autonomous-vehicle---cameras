# Librerías
import sensor
import time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)  
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(time=2000)
THRESHOLD = (150, 200)
clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD])

    rects = img.find_rects(threshold=10000) #Función find_rects buscará rectangulos que entren en el umbral de 10000.
    detect_rects = len(rects) #Cantidad de rectangulos obtenidos.
    print(detect_rects)

    for r in rects:
        if r.magnitude() > 60000 and (detect_rects > 4 and detect_rects < 6): #Si la cantidad de rectangulos y su magnitude son correctas, se dibujaran sus esquinas.
            #img.draw_rectangle(r.rect(), color=(255, 0, 0))
            for p in r.corners():
                img.draw_circle(p[0], p[1], 5, color=(0, 255, 0))
            print("Paso peatonal detectado",detect_rects)
