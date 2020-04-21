#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sym
from sympy import Symbol
from sympy import pprint


# In[2]:


#SEMBOLLEŞTİRDİL
p=Symbol('p')
x=Symbol('x')
n=Symbol('n')


# In[3]:


#Formulu parçalara ayırdık.
my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
my_f_3_part_0


# In[5]:


my_f_3_part_1=p**x
my_f_3_part_1


# In[6]:


my_f_3_part_2=(1-p)**(n-x)
my_f_3_part_2


# In[7]:


my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
my_f_3 #Formülün tamamı


# In[9]:


#Grafiğe döktük
sym.plot(my_f_3.subs({p:0.7,n:50}),(x,0,50),title='binomial distribution plot for n=50')


# In[14]:


from sympy import Symbol, Limit


# In[15]:


t=Symbol('t')
St= 5*t**2 + 2*t + 8 


# In[16]:


t1 = Symbol('t1')
delta_t = Symbol('delta_t')


# In[17]:


St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})


# In[18]:


Limit((St1_delta-St1)/delta_t,delta_t,0).doit() #İşleme soktuk


# In[19]:


from sympy import Symbol, exp,sqrt,pi,Integral


# In[20]:


x = Symbol('x')


# In[21]:


p = exp(-(x - 10)**2/2)/sqrt(2*pi)


# In[23]:


Integral(p, (x, 11 ,12)).doit().evalf()


# In[ ]:




