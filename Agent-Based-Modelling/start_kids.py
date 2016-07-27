# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:51:53 2016

@author: Usuario
"""
#Action
from kids import Kid

def print_possessions(kids):
    for kid in kids:
        print(kid.balls, end=" ")
    print()

names = ['Neylson', 'Bruna', 'Leonardo', 'Mel', 'Raquel', 'Jerônimo', 'Silvio',
        'Elaine', 'Maria', 'João']

kids = []

for i in names:
    kids.append(Kid(name = i, balls = 0))
    
kids[0].balls = 1

for i in range(9):
    num_balls = kids[i].give_ball(balls = 1)
    kids[i + 1].receive_ball(num_balls)
    print_possessions(kids)