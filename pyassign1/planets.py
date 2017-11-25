#!/usr/bin/env python3

"""planets.py: Draws ecliptic orbits of 6 planets around the sun.

__author__ = "Cai Jiaji"
__pkuid__ = "1700017797"
__email__ = "jiajicaiyp@pku.edu.cn"
"""

import turtle

def main():
    for t in [sun,merury,venus,earth,mars,jupiter,saturn]:
        t = turtle.Turtle()
        t.shape("circle")
    turtle.exitonclick()

if __name__ == "__main__":
    main()
