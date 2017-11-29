#!/usr/bin/env python3

"""planets.py: Draws ecliptic orbits of 6 planets around the sun.
__author__ = "Cai Jiaji"
__pkuid__ = "1700017797"
__email__ = "jiajicaiyp@pku.edu.cn"
"""

import turtle
import math


def place(t, a, b, o):
    c = math.sqrt(a**2-b**2)
    t.up()
    if o == "left":
        t.setpos(a+c, 0)
    if o == "right":
        t.setpos(a-c, 0)
    t.down()
    t.setheading(90)


def main():
    sun = turtle.Turtle()
    mercury = turtle.Turtle()
    venus = turtle.Turtle()
    earth = turtle.Turtle()
    mars = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturn = turtle.Turtle()

    for t in [sun, mercury, venus, earth, mars, jupiter, saturn]:
        t.shape("circle")
        t.speed(0)

    sun.color("yellow")
    mercury.color("blue")
    venus.color("green")
    earth.color("red")
    mars.color("black")
    jupiter.color("orange")
    saturn.color("cyan")

    place(mercury, 30, 30, "left")
    place(venus, 50, 40, "left")
    place(mars, 100, 75, "right")
    place(earth, 125, 50, "left")
    place(jupiter, 150, 30, "left")
    place(saturn, 175, 100, "left")

    for t in [sun, mercury, venus, earth, mars, jupiter, saturn]:
        t.forward(0.01)

    for j in range(4):
        for i in range(1000):
            for t in [mercury, venus, earth, mars, jupiter, saturn]:
                if t == mercury:
                    a, b = 30, 30
                if t == venus:
                    a, b = 50, 40
                if t == earth:
                    a, b = 100, 75
                if t == mars:
                    a, b = 125, 50
                if t == jupiter:
                    a, b = 150, 30
                if t == saturn:
                    a, b = 175, 100
                c = math.sqrt(a**2-b**2)
                circumference = math.pi*(3/2*(a+b)-math.sqrt(a*b))
                step = circumference/1000
                p = t.position()
                x = p[0]
                y = p[1]
                if t == mars:
                    angle_rad = math.pi + math.atan2(-b**2*(x+c/2), a**2*y)
                else:
                    angle_rad = math.pi + math.atan2(-b**2*(x-c/2), a**2*y)
                angle = math.degrees(angle_rad)
                t.setheading(angle)
                t.forward(step)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
