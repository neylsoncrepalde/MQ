# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:07:34 2016

@author: Usuario
"""
from dog import Dog
#Now, let's create a zoo.
zoo = []
names = ['Willi', 'James', 'Snoopy', 'Pateta', 'Floquinho', 'Pluto']

for name in names:
    zoo.append(Dog(name, 'mixed_breed'))

zoo.append(Dog('Jimmy', 'Pastor Alemão'))

#Create time

for time in range(100):
    for dog in range(len(zoo)):
        zoo[dog].bark()
    if time == 99:
        for i in range(len(zoo)):
            print(zoo[i].name)