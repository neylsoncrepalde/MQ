# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:44:10 2016

@author: Usuario
"""
#Defining class Kid
class Kid:
    def __init__(self, name, balls):
        self.balls = balls
        self.name = name
        
    def give_ball(self, balls):
        self.balls = self.balls - balls
        return balls
        
    def receive_ball(self, balls):
        self.balls = self.balls + balls