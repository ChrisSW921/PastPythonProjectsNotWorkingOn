"""This program shows us the relationship between how many steps we take and turns,
and how far our final position is from the origin. Looking at the relationship, we see that with
more steps that we take, the farther we are away. A formula I found online states that
Xk = ±1, with P(Xk = 1) = p and P(Xk = −1) = 1−p = q."""

from turtle import *
import random
import math
tracer(False)
import statistics
bgcolor("skyblue")
turns = [0,90,180,270]
Regs = [0,180]


def Go_Home():
    """This is just to eliminate common code"""
    stamp()
    penup()
    home()
    setheading(0)

def code(steps, runs, walk, nums):
    """This is the function that calculates the numbers
and plots the picture, depending on the arguements passed in"""
    Pas_Num = []
    Mi_Ma_Num = []
    Reg_Num = []
    for _ in range(runs):
        for _ in range(steps):
            if walk == "Reg":
                left(random.choice(Regs))
                penup()
                if nums == "yes":
                    forward(1)
                else:
                    forward(9)
            elif walk == "Pa":
                left(random.choice(turns))
                penup()
                if nums == "yes":
                    forward(1)
                else:
                    forward(9)        
            elif walk == "MiMa":
                left(random.choice(turns))
                if heading() == 270:    
                    penup()
                    if nums == "yes":
                        forward(2)
                    else:
                        forward(18)                   
                else:
                    penup()
                    if nums == "yes":
                        forward(1)
                    else:
                        forward(9)
                         
                                         
        if walk == "Reg":
            if nums == "yes":
                Reg_Num.append(distance(0,0))
                home()
                setheading(0)
            else:
                pendown()
                setheading(0)
                color("red")
                shape("triangle")
                Go_Home()          
        elif walk == "Pa":
            if nums == "yes":
                Pas_Num.append(distance(0,0))
                home()
                setheading(0)
            else:
                pendown() 
                color("black")
                shape("circle")
                Go_Home()
        elif walk == "MiMa":
            if nums == "yes":
                Mi_Ma_Num.append(distance(0,0))
                home()
                setheading(0)
            else:
                pendown()    
                color("green")
                shape("square")
                Go_Home()
    if walk == "Pa" and nums == "yes":
        print(f"Pa random walk of {steps} steps")
        print(f"Mean = {round(statistics.mean(Pas_Num), 1)}  CV = {round(statistics.stdev(Pas_Num),1)}")
        print(f"Max = {round(max(Pas_Num),1)}  Min = {round(min(Pas_Num),1)}\n")
    elif walk == "MiMa" and nums == "yes":
        print(f"Mi-Ma random walk of {steps} steps")
        print(f"Mean = {round(statistics.mean(Mi_Ma_Num),1)}  CV = {round(statistics.stdev(Mi_Ma_Num),1)}")
        print(f"Max = {round(max(Mi_Ma_Num),1)}  Min = {round(min(Mi_Ma_Num),1)}\n")
    elif walk == "Reg" and nums == "yes":
        print(f"Reg random walk of {steps} steps")
        print(f"Mean = {round(statistics.mean(Reg_Num),1)}  CV = {round(statistics.stdev(Reg_Num),1)}")
        print(f"Max = {round(max(Reg_Num),1)}  Min = {round(min(Reg_Num),1)}\n")
    
         
def Main():
    """This is the main function that calls the funcion"""
    code(100, 50, "Pa", "no")
    code(100, 50, "Pa", "yes")
    code(1000, 50, "Pa", "yes")
    code(100, 50, "MiMa", "no")
    code(100, 50, "MiMa", "yes")
    code(1000, 50, "MiMa", "yes")
    code(100, 50, "Reg", "no")
    code(100, 50, "Reg", "yes")
    code(1000, 50, "Reg", "yes")
    
    
if __name__ == "__main__":
    Main()