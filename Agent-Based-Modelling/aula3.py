# -*- coding: utf-8 -*-
"""
MQ - ABM
Aula3
Neylson
"""
class Dog:                          # Cuidado init com 2 underlines
    def __init__(self, name, breed): #Função que cria um novo cachorro
        self.name = name
        self.breed = breed
        self.has_bone = False
        self.memory = ""
        
    def hear(self, something):
        self.memory = something
        
    def take_bone(self):
        self.has_bone = True
        
    def drop_bone(self):
        if self.has_bone == True:
            self.has_bone = False
        
    def bark(self):
        if not(self.has_bone):
            print("WOWuff")
            
            
rex = Dog("Rex", "Chiwawa")
rex.bark()
rex.take_bone()
rex.hear("Reeex... Come here!")
rex.take_bone()
rex.drop_bone()


#Now, let's create a zoo.
zoo = []

names = ['Willi', 'James', 'Snoopy', 'Pateta', 'Floquinho', 'Pluto']

for name in names:
    zoo.append(Dog(name, 'mixed_breed'))

zoo[2].bark()

#Create time

for time in range(100):
    for dog in range(6):
        print(zoo[dog].bark)


#Programming a kids class
class Kid:
    def __init__(self, name, balls):
        self.balls = balls
        self.name = name
        
    def give_ball(self, balls):
        self.balls = self.balls - balls
        return balls
        
    def receive_ball(self, balls):
        self.balls = self.balls + balls
        

#Action
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


