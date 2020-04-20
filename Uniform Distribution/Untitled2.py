#!/usr/bin/env python
# coding: utf-8

# In[30]:


from sympy import Symbol, pprint, Piecewise
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt
import math

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
f = 1 / abs(a-b)
pprint(f)

x_values=9
y_values=3
if(x_values>y_values):
    x_values,y_values=y_values,x_values
syp.plot(Piecewise((0, (x < x_values) | (x > y_values)), (f.subs({a:x_values, b: y_values}), (x >= x_values) & 
        (x <= y_values))), (x, -10, 10), title="uniform_distribution_sympy")


# In[ ]:




