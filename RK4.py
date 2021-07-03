# Amo a programar un runge kutta #
import numpy as np
import matplotlib.pyplot as plt
from Numeric import *
import sys
import math

def f(x,y):
    return x+y     # Esto devuelve la funcion que pongamos

def RK4(x0,y0,xn,n):

    #Tamaño paso#
        h = (xn-x0)/n  
        print('\n--------SOLUTION--------')
        print('------------------------')    
        print('x0\ty0\tyn')
        print('-------------------------')
        for i in range(n):
            k1 = h * (f(x0, y0))
            k2 = h * (f((x0+h/2), (y0+k1/2)))
            k3 = h * (f((x0+h/2), (y0+k2/2)))
            k4 = h * (f((x0+h), (y0+k3)))
            k = (k1+2*k2+2*k3+k4)/6
            yn = y0 + k
            print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
            print('-------------------------')
            y0 = yn
            x0 = x0+h
        
        print('\nAt x=%.4f, y=%.4f' %(xn,yn))

def plot_diagram():
	global x
	t = 0.0
	h = 0.1
	for value in arange(0.1,5.0,0.1):
		l = calculate_rungekutta_param(x,t,h)
		x = x + l
		x_value.append(x)
		t = t + h
		t_value.append(t)
		
	
	t = np.arange(0.0, 5.0, 0.1)
	x_derivatives = np.arange(-15.0, 30.0, 1.0)
	plt.figure(1)
	plt.subplot(111)
	plt.xlabel('time (t) ')
	plt.ylabel('displacement (x) ')
	plt.title('Graph Between X and t')
	plt.plot(t_value,x_value)
	
	plt.figure(2)
	plt.subplot(211)
	plt.xlabel('value of x (x)')
	plt.ylabel('value of x_das (y) ')
	plt.title('Graph Between X derivatives and x')
	plt.plot(x_derivatives,f(t0,x_derivatives))
	plt.axis([-25.0, 25.0,-600.0,0.0])
	plt.show()

# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# RK4 method call
RK4(x0,y0,xn,step)