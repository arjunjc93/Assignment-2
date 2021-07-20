# -*- coding: utf-8 -*-
"""Collinear1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CuYS_uQbaHTtZzTKB4cgfQiLFv0jKLTS
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([2,8,-3,5])

plt.axis('on')
plt.grid(True)

A = np.array([7,-2])
B = np.array([5,1])
C = np.array([3,4])

def line_gen(A,B):
   len =10
   dim = (A.shape[0])
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
   return x_AB

  #Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.text(7,-2,'A (7,-2)')
plt.text(5,1,'B (5,1)')
plt.text(3,4,'C (3,4)')

plt.savefig('collinear1.pdf')
plt.show()