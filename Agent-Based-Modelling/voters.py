#ABM
#Voters
from turtle import Turtle
from random import randrange
from numpy import argmin

class Voter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        turtle = Turtle()
        turtle.speed('fastest')
        turtle.color('blue')
        turtle.penup()
        turtle.goto(x, y)
        turtle.hideturtle()
        turtle.dot()
        
    def vote(self, politicians):
        dist = []        
        for politician in politicians:
            d = ((politician.x - self.x)**2 + 
            (politician.y - self.y)**2)**0.5
            dist.append(d)
        return argmin(dist)
