#!/usr/bin/env python2

from swampy.TurtleWorld import *
from polygon import arc

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        rt(t, 360.0/n)


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

move(bob, -150)
petal(bob, 50.0, 100.0)
move(bob,100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 200)
flower(bob, 50, 50.0, 100.0)

bob.die()
wait_for_user()