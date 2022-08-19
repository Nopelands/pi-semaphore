import RPi.GPIO as GPIO
import time
import json
import socket as s
import os
import datetime

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
    
car_log = open("car_log.txt", "a+")
    
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
try:
    socket.bind(('127.0.0.1', 2035))
except s.error:
    print("Failed to bind")
    sys.exit()
socket.setblocking(False)
socket.listen()

def get_config(json_data):
    config = [json_data["red_time"], json_data["yellow_time"], json_data["green_time"]]
    user_log = open("user_log.txt", "a")
    user_log.write(f"{json_data['username']} - {datetime.datetime.now()}")
    user_log.close()
    return config
    
def reply_request():
    pass

def display_write(time):
    if time > 9:
        time = 9
    number1 = int(time % 10)
    segmentos1 = sete_segmentos[number1]
    for i in range(len(display1)):
        GPIO.output(display1[i], segmentos1[i])

config = [1, 1, 1]
state = "red"
state_time = 0
previous_movement = 0
car_log = open("car_log.txt", "r")
car_log_count = [int(i) for i in car_log.read().split(" ")]
car_log.close()

while True:
    try:
        conn,addr = socket.accept()
        data = conn.recv(4096)
        json_data = json.loads(data)
        print(json_data)
        if json_data["command"] == "SETUP":
            config = get_config(json_data)
        elif json_data["command"] == "GETDATA":
            reply_request(json_data)
    except:
        pass
    red_time = config[0]
    yellow_time = config[1]
    green_time = config[2]
    print(state)
    if state == "red":
        time.sleep(0.1)
        state_time += 0.1
        if state_time >= red_time:
            state = "green"
            state_time = 0
            previous_movement = 0
    elif state == "yellow":
        time.sleep(0.1)
        state_time += 0.1
        if state_time >= yellow_time:
            state = "red"
            state_time = 0
            previous_movement = 0
    elif state == "green":
        time.sleep(0.1)
        state_time += 0.1
        display_write(int(green_time - state_time))
        if state_time >= green_time:
            state = "yellow"
            state_time = 0
            previous_movement = 0
    mov_read = GPIO.input(mov_sensor)
    if mov_read != previous_movement and previous_movement == 0 and state != "yellow":
        if state == "red":
            car_log_count[0] += 1
        else:
            car_log_count[1] += 1
        car_log = open("car_log.txt", "w")
        car_log.write(f"{car_log_count[0]} {car_log_count[1]}")
        car_log.close()
        print(car_log_count)
    previous_movement = mov_read
