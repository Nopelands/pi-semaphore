import RPi.GPIO as GPIO
import time

green = 1
red = 2
yellow = 3

buzzer = 4

A1 = 5
B1 = 6
C1 = 7
D1 = 8
E1 = 9
F1 = 10
G1 = 11

A2 = 12
B2 = 13
C2 = 14
D2 = 15
E2 = 16
F2 = 17
G2 = 18

trigger = 19
echo = 20

sete_segmentos[10][7] = [
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
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(C1, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(E1, GPIO.OUT)
GPIO.setup(F1, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(C2, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(E2, GPIO.OUT)
GPIO.setup(F2, GPIO.OUT)
GPIO.setup(G2, GPIO.OUT)

while True:
    pass()