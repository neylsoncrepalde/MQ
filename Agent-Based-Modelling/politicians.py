#ABM
#Politicians
from turtle import Turtle
from numpy.random import normal

class Politician:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.turtle = Turtle()
        self.turtle.color('black')
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.votes = 0
        self.wins = 0
        
    def readjust_after_election(self, win, winner):        
        if win == True:
            self.turtle.color('green')
        else:
            self.turtle.color('red')
            self.x = winner.x*0.5 + self.x*0.5
            self.y = winner.y*0.5 + self.y*0.5
            self.turtle.goto(self.x, self.y)
