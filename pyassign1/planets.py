#!/usr/bin/env python3

"""planets.py: Draws ecliptic orbits of 6 planets around the sun.

__author__ = "Cai Jiaji"
__pkuid__ = "1700017797"
__email__ = "jiajicaiyp@pku.edu.cn"
"""

import turtle
import math


def eclipse(t, a, b, s, o, n):
    c = math.sqrt(a**2-b**2)
    circumference = math.pi*(3/2*(a+b)-math.sqrt(a*b))
    step = circumference/n

    t.up()
    if o == "left":
        t.setpos(a+c, 0)
    if o == "right":
        t.setpos(a-c, 0)

    t.down()
    t.setheading(90)
    t.speed(s)
    t.forward(step)

    for j in range(4):
        for i in range(n):
            p = t.position()
            x = p[0]
            y = p[1]
            if o == "left":
                angle_rad = math.pi + math.atan2(-b**2*(x-c/2), a**2*y)
            if o == "right":
                angle_rad = math.pi + math.atan2(-b**2*(x+c/2), a**2*y)
            angle = math.degrees(angle_rad)
            t.setheading(angle)
            t.forward(step)


def main():
    sun = turtle.Turtle()
    mercury = turtle.Turtle()
    venus = turtle.Turtle()
    earth = turtle.Turtle()
    mars = turtle.Turtle()
    jupiter = turtle.Turtle()
    saturn = turtle.Turtle()

    sun.shape("circle")
    mercury.shape("circle")
    venus.shape("circle")
    earth.shape("circle")
    mars.shape("circle")
    jupiter.shape("circle")
    saturn.shape("circle")

    sun.color("yellow")
    mercury.color("blue")
    venus.color("green")
    earth.color("red")
    mars.color("black")
    jupiter.color("orange")
    saturn.color("cyan")

    eclipse(mercury, 30, 30, 0, "left", 1000)
    eclipse(venus, 50, 40, 0, "left", 1000)
    eclipse(mars, 100, 75, 0, "right", 1000)
    eclipse(earth, 125, 50, 0, "left", 1000)
    eclipse(jupiter, 150, 30, 0, "left", 1000)
    eclipse(saturn, 175, 100, 0, "left", 1000)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
