#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:31:31 2020
Module: AST40007W-Computaional Methods 
#Shooting Method Project.  
@author: Chad Thomas <thmcha014>
"""

#Importing packages.
import numpy as np 
import matplotlib.pyplot as plt 

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

#Initial Values.
t0      = 0
y0      = 0
v0      = 1         #y_prime initial value
h       = 0.05
Lambda1 = 8

#Creating arrays to store the values as we step throught the function.
lambda_values = np.arange(t0, Lambda1 + h, h)
y_values      = np.zeros(lambda_values.size)
v_values      = np.zeros(lambda_values.size)

#Assigning the first few values of the arrays.
lambda_values[0]    = t0
y_values[0]         = y0 
v_values[0]         = v0

#The ODE function
def f1(t, y, v):
    return v

def f2(t, y, v):
    return (t-Lambda1)*y

for i,t in enumerate(y_values[:-1]):
    y_values[i + 1] = y_values[i] + h * f1(t, y_values[i], v_values[i])
    v_values[i + 1] = v_values[i] + h * f2(t, y_values[i], v_values[i])
    
    
print(lambda_values)
#Plotting the solution
#fig, ax = plt.subplots(3,1, sharex = True, figsize = (10, 10))

plt.plot(lambda_values, v_values, 'green', linewidth=2)
plt.title('Lambda = 8')
plt.ylabel('y(x)')
plt.xlabel('x')
plt.legend()
#plt.savefig('Tut7_Q1_1<thmcha014>.png')
plt.show()

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

Lambda2  = 12

#Creating arrays to store the values as we step throught the function.
lambda_values = np.arange(t0, Lambda2 + h, h)
y_values      = np.zeros(lambda_values.size)
v_values      = np.zeros(lambda_values.size)

#Assigning the first few values of the arrays.
lambda_values[0]    = t0
y_values[0]         = y0 
v_values[0]         = v0

#The ODE function
def f1(t, y, v):
    return v

def f2(t, y, v):
    return (t-Lambda2)*y

for i,t in enumerate(y_values[:-1]):
    y_values[i + 1] = y_values[i] + h * f1(t, y_values[i], v_values[i])
    v_values[i + 1] = v_values[i] + h * f2(t, y_values[i], v_values[i])
    
    
print(lambda_values)
#Plotting the solution
#fig, ax = plt.subplots(3,1, sharex = True, figsize = (10, 10))

plt.plot(lambda_values, v_values, 'green', linewidth=2)
plt.title('Lambda = 12')
plt.ylabel('y(x)')
plt.xlabel('x')
plt.legend()
#plt.savefig('Tut7_Q1_1<thmcha014>.png')
plt.show()

#------------------------------------------------------------------------------















