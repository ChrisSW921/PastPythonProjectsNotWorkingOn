"""
Welcome to my program! If you run it from the thonny window, you will see no celestial bodies, but,
depending on what you put in the shell arguements, you will begin to see them!

Instructions for shell window:

python main.py <moon or sun or tatooine>

Side note: When run in shell window, the picture appears zoomed in, which Dr R said was ok.
As well, if you decide to run the code in the thonny window, you will get an error on line 194, this
error is to be ignored, it is simply saying you dont have any arguements from command line."""

from turtle import *
import random
from sys import argv
tracer(False)
bgcolor("sky blue")


house_width = 60
house_height = 70
mini_house_width = 30
mini_house_height = 35
tree_colors = ["green yellow", "chartreuse", "orange red", "lime"]
colors = ["green yellow", "gray", "cornflower blue", "sienna", "yellow", "orange", "brown", "mint cream"]
    

def begin():
    """Puts the turtle where it needs to go"""
    penup()        
    goto(-900, -375)
    pendown()

def rectangle(size1, size2, color1):
    """
Draws a rectangle
"""
    speed(0)
    color(color1)
    begin_fill()
    for _ in range(2):
        forward(size1)
        left(90)
        forward(size2)
        left(90)
    end_fill()

def triangle(size1, color1):
    """
Draws a triangle
"""
    speed(0)
    color(color1)
    begin_fill()
    for _ in range(3):
        forward(size1)
        left(120)
    end_fill()
    
def square(size1):
    """
Draws a square
"""
    speed(0)
    color(colors[6])
    begin_fill()
    for _ in range(4):
        forward(size1)
        left(90)
    end_fill()
    
def tree():
    """Draws a tree"""
    tree_size = random.randint(10, 17)
    square(tree_size)
    left(90)
    forward(tree_size)
    left(90)
    forward(tree_size)
    right(180)
    triangle((tree_size * 3), random.choice(tree_colors))
    penup()
    forward(tree_size * 4)
    right(90)
    forward(tree_size)
    left(90)
    penup()
    

def house(width, height, color1, color2, color3):
    """Draws a house"""
    rectangle(width, height, color3)
    turn()
    forward(height)
    right(90)
    pendown()
    triangle(width, color1)
    right(90)
    penup()
    forward(height)
    left(90)
    forward(width / 2)
    pendown()
    rectangle((width / 5), (height / 5), color2)
    penup()
    forward(width)
    
    
def street(width, height, color1, color2, color3, houses):
    """Draws multiple houses in a line"""
    for _ in range(houses):
        house(width, height, color1, color2, color3)
        
def tree_row(x):
    """Draws multiple trees"""
    for _ in range(x):
        tree()
        
        
def sun(color1 = colors[4], color2 = colors[4]):
    """Draws a sun"""
    color(color1, color2)
    begin_fill()
    circle(50)
    end_fill()
    
def moon():
    """Draws a moon"""
    color(colors[7], colors[7])
    begin_fill()
    circle(50, 180)
    end_fill()
        
def turn():
    """Turns turtle 90 degrees"""
    penup()
    left(90)
    
def tatooine():
    """Draws two suns"""
    sun(colors[4], colors[4])
    forward(100)
    sun(colors[5], colors[5])
    
def mountain_1():
    """Draws mountains"""
    triangle(random.randint(50,100), colors[1])
    forward(100)
    triangle(random.randint(150,300), colors[1])
    
def mini_scene():
    """Draws mountains, trees and houses"""
    mountain_1()
    tree_row(random.randint(1, 3))
    street(mini_house_width, mini_house_height, colors[2], colors[2], colors[3], random.randint(1,2))
        
def main():
    """Draws everything"""
    screen = Screen()
    screen.setup(width = 1.0, height = 1.0)
    penup()
    goto(-960,0)
    color("green")
    begin_fill()
    pendown()
    forward(window_width() * 2)
    right(90)
    forward(window_height())
    right(90)
    forward(window_width() * 2)
    right(90)
    forward(window_height())
    end_fill()
    right(90)
    mini_scene()
    forward(400)
    mini_scene()
    forward(400)
    mini_scene()
    speed(0)
    begin()
    street(house_width, house_height, colors[1], colors[2], colors[3], 20)
    begin()
    turn()
    forward(house_height * 4)
    right(90)
    pendown()
    tree_row(43)
    begin()
    turn()
    forward(house_height * 10)
    right(90)
    forward(house_height * 10)
    if argv[1] == "moon":
        bgcolor("blue")
        moon()
    elif argv[1] == "sun":
        sun()
    elif argv[1] == "tatooine":
        tatooine()
    mainloop()
        
    
if __name__ == "__main__":    
    main()
    

    
    
    

    


