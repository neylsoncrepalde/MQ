#ABM
#Politicians
from turtle import Turtle

class Politician:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.turtle = Turtle()
        self.turtle.speed('fastest')
        self.turtle.color('red')
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        
