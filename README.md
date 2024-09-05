# Cámaras para vehículo de conducción autónoma

## Descripción

Programas de OpenMV (MicroPython) orientado al microcontrolador Nicla Vision de la familia Arduino Pro. Se tiene un total de 3 programas para la detección de líneas, detección de paso peatonal y comunicación I2C (esclavo); con ello dará la información necesaria al microcontrolador maestro para hacer un correcto seguimiento de líneas y parada ante cruces; para modificar la velocidad y dirección del vehículo autónomo a escala.

## Hardware

El programa esta diseñado para establecer comunicación con un arduino Mega, Uno o Nano, sin embargo, lo programas de detección son exclusivos de la Nicla Vision.

## Librerías

- [sensor](https://docs.openmv.io/library/omv.sensor.html#module-sensor)
- [time](https://docs.openmv.io/library/time.html#module-time)
- [pyb](https://docs.openmv.io/library/pyb.html#module-pyb)
    - [Pin](https://docs.openmv.io/library/pyb.LED.html#pyb.LED)
- [machine](https://docs.openmv.io/library/machine.html#module-machine)
    - [I2C](https://docs.openmv.io/library/machine.I2C.html)
    - [LED](https://docs.openmv.io/library/machine.Pin.html)
- [image](https://docs.openmv.io/library/omv.image.html#module-image)
- [math](https://docs.openmv.io/library/math.html#module-math)
