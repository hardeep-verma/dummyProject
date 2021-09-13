import numpy as np
import math as m
import  matplotlib.pyplot as plt

# Secant method

def f(x) :
    return (2*x*x-5*x+3)
x1= float(input("enter intial value "))
x2= float(input("enter second value "))
print(f(x2))
print(f(x1))
for i in range(50):
     x3= x2-(x2-x1)*f(x2)/(f(x2)-f(x1))
     if abs(x3-x2)<0.001: break

     else:
         x1=x2
         x2=x3
print('the final root = ',x3)
print('no. of iteration = ',i)

# Bisection method
def f(x) :
    return(3*x + m.sin(x) - m.exp(x))
x1=float(input("enter intial value "))
x2=float(input('enter second value '))
if f(x1)*f(x2)<0:
    for i in range(6) :
        x3=(x1+x2)*0.5
        if f(x3)*f(x1)<0:
            x2=x3
        else:x1=x3
print(x3)

# newton Raphson Method


