# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:54:00 2022

@author: Gabriele Merrcolino
"""

import turtle

def tree(pen, lenght, rotation, level):
    pen.down()
    if(level <= 0):
        pen.dot(5, (0,0,0))
        return
    
    pen.forward(lenght)
    pen.left(rotation)
    
    tree(pen, lenght * .8, rotation, level-1)

    pen.right(rotation*2)
    
    tree(pen, lenght * .8, rotation, level-1)
    
    pen.left(rotation)
    pen.up()
    pen.backward(lenght)


pen = turtle.Turtle()

pen.speed(0)

for i in range(10):
    pen.clear()
    
    for _ in range(8):
        
        tree(pen, 50, 20, i+1)
        
        pen.right(45)
