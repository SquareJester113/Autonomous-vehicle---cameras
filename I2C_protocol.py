# I2C Control
# Basado en el ejemplo proporcionado por el software OpenMV

#Librerías
from machine import I2C, Pin, LED
import machine
import time
import math

# Variable global y pines de comunicación SDA y SCL
global address
SDA = Pin('PB9', Pin.OPEN_DRAIN)
SCL = Pin('PB8', Pin.OPEN_DRAIN)

#Activación de los pines en configuración Pull_UP
SDA.PULL_UP
SCL.PULL_UP

#Inicialización de los pines en configuración Open drain y en formato Pull up
SDA.init(Pin.OPEN_DRAIN, Pin.PULL_UP)
SCL.init(Pin.OPEN_DRAIN, Pin.PULL_UP)
clock = time.clock()
ledR = LED("LED_RED")
ledB = LED("LED_BLUE")

#Establecimiento del protocolo I2C, usando los pines deseados
i2c = machine.SoftI2C(scl=SCL,sda=SDA,freq=9600,timeout=9600)#100000)
print(i2c)

#Nota: usa pines PB9 y PB8 porque es la única combinación de pines que me funcionó.

#Inicias la comunicación
i2c.init(scl=SCL,sda=SDA,freq=9600)

#Escaneo para determinar las direcciones existentes (Conectar el arduino a usar)
list_I2C = i2c.scan()
if(list_I2C[0] == None):
    print("Dirección no encontrada")
    address = 14 #Puedes modificarla con la dirección de tu arduino.
else:
    print("Conexión exitosa")
    address = list_I2C[0]

def Busqueda(): #Función de busqueda de señales
    add = address
    while(add == None or add != 14):
        print("Buscando...")
        list_S = i2c.scan() #Lista de señales detectadas.
        print(list_S)
        add = list_S[0] #Ingreso de la primera dirección de la lista.
        print(add)
        if(address == 14): #El 14 es mi dirección, modificala de ser necesario.
            print("Dirección detectada:",add)

def conexionLetras(dato): #Envío de un único carácter ASCII.
    ASCII = ord(dato)
    dato_bytes = bytes([ASCII])
    try:
        ledB.on()
        i2c.start()
        i2c.writeto(address,dato_bytes)
        #print("Enviado")
        time.sleep(2)
        i2c.stop()
        ledB.off()
        return
    except Exception as e:
        print("Error de envio, favor de reiniciar",dato_bytes,"Error:",e)
        return

def conexionNumeros(num): #Envío de datos númericos enteros.
    if not isinstance(num, int):
            print("Error: El dato debe ser un número entero.")
            return

    num_bits = math.ceil(math.log2(num + 1))
    num_bytes = (num_bits + 7) // 8 #Calculo de bytes necesarios para el numero
    Numero_bytes = num.to_bytes(num_bytes, 'big') #Conversión del número a bytes

    try:
        ledB.on()
        i2c.start()
        # Enviar los datos en formato de bytes
        i2c.writeto(address, Numero_bytes)
        #print("Enviado")
        time.sleep(2)
        i2c.stop()
        ledB.off()
        return
    except Exception as e:
        print("Error de envio, favor de reiniciar", num, e)
        return

def Conexion(dato): #Función usada para el envío de datos tipo ASCII
    try:
        ledB.on()
        i2c.start() #Necesario para iniciar comunicación

        if isinstance(dato, str) and len(dato) == 1:
            ASCII = ord(dato)
            dato_bytes = bytes([ASCII])
            print("Enviando carácter:", dato)
        elif isinstance(dato, int):
            num_bits = math.ceil(math.log2(dato + 1))
            num_bytes = (num_bits + 7) // 8 #Calculo de bytes necesarios para el numero
            dato_bytes = dato.to_bytes(num_bytes, 'big') #Conversión de dato a byte.
            print("Enviando número:", dato)
        else:
            print("Error: El dato debe ser un carácter o un número entero.")
            return

        # Enviar los datos en formato de bytes
        i2c.writeto(address, dato_bytes)
        time.sleep(2)
        i2c.stop()
        ledB.off()
        return
    except Exception as e:
        print("Error de envio",dato,"Error:",e)
        return

while True: #Función principal
    clock.tick()

    if(address == None and address != 14): #Descarta el proceso de no existir conexión.
        ledR.on()
        print("Error de conexión, favor de reiniciar")
        break
    else:
        #print("Enlazado",address)
        try: #Intenta un envío de datos usando las funciones
            ledB.on() #Marca el inicio encendiendo el LED interno en color azul
            i2c.start()
            conexionLetras(dato = 'H')
            time.sleep_ms(500)
            conexionNumeros(num = 150)
            i2c.stop()
            ledB.off()
            time.sleep_ms(300)
        except Exception as e:
            ledR.on() #Si falla enciende el de color rojo
            print("Error:",e)
            pass
            break
    #time.sleep(0.5)

# --------------------------------------------------------------------------------------------
# Nota: Estuve intentando varios métodos de establecer una comunicación de recepción sin éxito, 
# si deseas intentarlo te recomiendo leas la documentación del protocolo I2C - machine module.
# --------------------------------------------------------------------------------------------
# La comunicación resulto ser efectiva entre ambas placas, mi ultima recomendación es cuidar que 
# la conexión entre ambas placas sea correcta, para ello se recomienda la revisión de los pines
# de la [Nicla Vision](https://content.arduino.cc/assets/Pinout_NiclaVision_latest.png)
