import RPi.GPIO as GPIO
import time

green = 1
red = 2
yellow = 3

buzzer = 4

display1 = [5, 6, 7, 8, 9, 10, 11]
display2 = [12, 13, 14, 15, 16, 17, 18]

trigger = 19
echo = 20

sete_segmentos = [
    [ 1,1,1,1,1,1,0 ], # = Digito 0
    [ 0,1,1,0,0,0,0 ], # = Digito 1
    [ 1,1,0,1,1,0,1 ], # = Digito 2
    [ 1,1,1,1,0,0,1 ], # = Digito 3
    [ 0,1,1,0,0,1,1 ], # = Digito 4
    [ 1,0,1,1,0,1,1 ], # = Digito 5
    [ 1,0,1,1,1,1,1 ], # = Digito 6
    [ 1,1,1,0,0,0,0 ], # = Digito 7
    [ 1,1,1,1,1,1,1 ], # = Digito 8
    [ 1,1,1,1,0,1,1 ], # = Digito 9
]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
for output in display1:
    GPIO.setup(output, GPIO.OUT)
for output in display2:
    GPIO.setup(output, GPIO.OUT)

def distance():
    GPIO.output(trigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(echo) == 0:
        StartTime = time.time()

    while GPIO.input(echo) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    distance = (TimeElapsed * 34300) / 2

    return distance

def display_write(centimeters):
    if centimeters > 99:
        centimeters = 99
    number1 = int(centimeters/10)
    number2 = centimeters % 10
    segmentos1 = sete_segmentos[number1]
    segmentos2 = sete_segmentos[number2]
    for i in range(len(display1)):
        GPIO.output(display1[i], segmentos1[i])
    for i in range(len(display2)):
        GPIO.output(display2[i], segmentos2[i])

while True:
    dist = distance()
    display_write(dist)
    if dist == 0:
        GPIO.output(red, 1)
        GPIO.output(yellow, 1)
        GPIO.output(green, 1)
        time.sleep(1)
        GPIO.output(red, 0)
        GPIO.output(yellow, 0)
        GPIO.output(green, 0)
    elif dist <= 33:
        GPIO.output(red, 1)
        GPIO.output(yellow, 0)
        GPIO.output(green, 0)
    elif dist <= 66:
        GPIO.output(red, 0)
        GPIO.output(yellow, 1)
        GPIO.output(green, 0)
    else:
        GPIO.output(red, 0)
        GPIO.output(yellow, 0)
        GPIO.output(green, 1)
    