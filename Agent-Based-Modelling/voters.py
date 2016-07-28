#ABM
#Voters
from turtle import Turtle
from random import randrange

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
        
    def vote(self):
        return randrange(0,5)