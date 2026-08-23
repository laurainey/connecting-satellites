import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600


TITLE = "Space satellites"

start_time = 0
total_time = 0
current_satellite = 0
number_satellites = 8 

satellites = []
lines = []

def create_satellites():
    global start_time
    for i in range (number_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40,760),randint(40,560)
        satellites.append(satellite)
    start_time = time()


def draw():
    global start_time, total_time
    screen.blit("space", (0,0))
    for satellite in satellites :
        satellite.draw()
        num = 1
        screen.draw.text(f"{num}",(satellite.pos[0],satellite.pos[1] + 20 ))
        num += 1
    if current_satellite < number_satellites :
        total_time = time() - start_time
        screen.draw.text(f"{round(total_time,1)}",(10,10),fontsize = 30)

    else:
        screen.draw.text(f"{round(total_time,1)}",(10,10),fontsize = 30)

def update() :
    pass



pgzrun.go()
