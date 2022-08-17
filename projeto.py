import RPi.GPIO as GPIO
import time
import json
import socket

green = 15
red = 11
yellow = 13

mov_sensor = 40

display1 = [23, 29, 31, 33, 35, 37, 12]

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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(mov_sensor, GPIO.IN)
for output in display1:
    GPIO.setup(output, GPIO.OUT)

def get_config():
    pass

def reply_request():
    pass

def display_write(time):
    if time > 9:
        time = 9
    number1 = int(time % 10)
    segmentos1 = sete_segmentos[number1]
    for i in range(len(display1)):
        GPIO.output(display1[i], segmentos1[i])

red_time = 1
yellow_time = 1
green_time = 1
state = "red"
state_time = 0
previous_movement = 0
car_log = {"red": 0, "green": 0}
config_log = {"name": [], "time": []}

while True:    
    config = get_config() # if socket?
    reply_request() # if?
    if state == "red":
        time.sleep(0.1)
        state_time += 0.1
        if state_time == red_time:
            state = "green"
            state_time = 0
            previous_movement = 0
    elif state == "yellow":
        time.sleep(yellow_time)
        state = "red"
        state_time = 0
    elif state == "green":
        time.sleep(0.1)
        state_time += 0.1
        display_write(int(green_time - state_time))
        if state_time == green_time:
            state = "yellow"
            state_time = 0
            previous_movement = 0

    mov_read = GPIO.input(mov_sensor)
    if mov_read != previous_movement and previous_movement == 0 and state != "yellow":
        car_log[state] += 1
    previous_movement = mov_read

