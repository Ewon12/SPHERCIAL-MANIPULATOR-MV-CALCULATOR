"""
Filename: FK_SMMV.py
Created on Wednesday 25/05/2022
Title: Forward Kinematics of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
a1 = 10mm
a2 = 40mm
a3 = 40mm
T1 = 45degrees
T2 =-20degrees
d3 = 40mm
"""

import numpy as np
import math

DHPT = [[(float(45)/180.0)*np.pi, (90.0/180.0)*np.pi, 0, float(10)],
       [(float(-20)/180.0)*np.pi+(90.0/180.0)*np.pi, (90.0/180.0)*np.pi,float(40), 0],
       [(0.0/180.0)*np.pi, (0.0/180.0)*np.pi,0, float(40)+float(40)]]

H0_1 =[
      [np.cos(DHPT[0][0]),-np.sin(DHPT[0][0])*np.cos(DHPT[0][1]),np.sin(DHPT[0][0])*np.sin(DHPT[0][1]),DHPT[0][2]*np.cos(DHPT[0][0])],
      [np.sin(DHPT[0][0]),np.cos(DHPT[0][0])*np.cos(DHPT[0][1]),-np.cos(DHPT[0][0])*np.sin(DHPT[0][1]),DHPT[0][2]*np.sin(DHPT[0][0])],
      [0,np.sin(DHPT[0][1]),np.cos(DHPT[0][1]),DHPT[0][3]],
      [0,0,0,1]
      ]
H1_2 =[
      [np.cos(DHPT[1][0]),-np.sin(DHPT[1][0])*np.cos(DHPT[1][1]),np.sin(DHPT[1][0])*np.sin(DHPT[1][1]),DHPT[1][2]*np.cos(DHPT[1][0])],
      [np.sin(DHPT[1][0]),np.cos(DHPT[1][0])*np.cos(DHPT[1][1]),-np.cos(DHPT[1][0])*np.sin(DHPT[1][1]),DHPT[1][2]*np.sin(DHPT[1][0])],
      [0,np.sin(DHPT[1][1]),np.cos(DHPT[1][1]),DHPT[1][3]],
      [0,0,0,1]
      ]
H2_3 =[
      [np.cos(DHPT[2][0]),-np.sin(DHPT[2][0])*np.cos(DHPT[2][1]),np.sin(DHPT[2][0])*np.sin(DHPT[2][1]),DHPT[2][2]*np.cos(DHPT[2][0])],
      [np.sin(DHPT[2][0]),np.cos(DHPT[2][0])*np.cos(DHPT[2][1]),-np.cos(DHPT[2][0])*np.sin(DHPT[2][1]),DHPT[2][2]*np.sin(DHPT[2][0])],
      [0,np.sin(DHPT[2][1]),np.cos(DHPT[2][1]),DHPT[2][3]],
      [0,0,0,1]
      ]


H0_1 = np.matrix(H0_1)
H1_2 = np.matrix(H1_2)
H2_3 = np.matrix(H2_3)
H0_2 = np.dot(H0_1, H1_2)
H0_3 = np.dot(H0_2, H2_3)
print("HTM = ")
print(np.matrix(np.around(H0_3,3)))
print("Position Vector")
X0_3 = H0_3[0,3]
print('X =',np.around(X0_3,3))
Y0_3 = H0_3[1,3]
print('Y =',np.around(Y0_3,3))
Z0_3 = H0_3[2,3]
print('Z =',np.around(Z0_3,3))