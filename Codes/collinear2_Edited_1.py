# -*- coding: utf-8 -*-
"""Collinear2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DYwMvFKt0-ARSbsQHoOfnNo0VJu5-FFG
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([1,9,-6,2])

plt.axis('on')
plt.grid(True)

A = np.array([8,1])
B = np.array([3,-4])
C = np.array([2,-5])

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

plt.text(8,1,'A (8,1)')
plt.text(3,-4,'B (3,-4)')
plt.text(2,-5,'C (2,-5)')

plt.savefig('collinear2.pdf')
plt.show()