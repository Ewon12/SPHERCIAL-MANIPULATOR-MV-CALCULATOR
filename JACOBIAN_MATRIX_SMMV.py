"""
Filename: JM_SMMV.py
Created on Wednesday 25/05/2022
Title: Jacobian Matrix of Spherical Manipulator - Modern Variant
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

Z_1 = [[0],[0],[1]] 
J1a = [[1,0,0], [0,1,0],[0,0,1]]
J1a = np.dot(J1a,Z_1)
J1b_1 = H0_3[0:3,3:]
J1b_1 = np.matrix(J1b_1)
J1b_2 = [[0],[0],[0]]
J1b=J1b_1-J1b_2
J1 = [[(J1a[1,0]*J1b[2,0])-(J1a[2,0]*J1b[1,0])],
     [(J1a[2,0]*J1b[0,0])-(J1a[0,0]*J1b[2,0])],
     [(J1a[0,0]*J1b[1,0])-(J1a[1,0]*J1b[0,0])]]
J2a = H0_1[0:3,0:3]
J2a = np.dot(J2a,Z_1)
J2b_1 = H0_3[0:3,3:]
J2b_1 = np.matrix(J2b_1)
J2b_2 = H0_1[0:3,3:]
J2b_2 = np.matrix(J2b_2)
J2b=J2b_1-J2b_2
J2 = [[(J2a[1,0]*J2b[2,0])-(J2a[2,0]*J2b[1,0])],
     [(J2a[2,0]*J2b[0,0])-(J2a[0,0]*J2b[2,0])],
     [(J2a[0,0]*J2b[1,0])-(J2a[1,0]*J2b[0,0])]]
J3 = H0_2[0:3,0:3]
J3 = np.dot(J3,Z_1)
J3 = np.matrix(J3)
J4= [[1,0,0], [0,1,0],[0,0,1]]
J4 = np.dot(J4,Z_1)
J4 = np.matrix(J4)
J5 = H0_1[0:3,0:3]
J5 = np.dot(J5,Z_1)
J6 = [[0],[0],[0]]
J6 = np.matrix(J6)
JM1 =np.concatenate((J1,J2,J3),1)
JM2 = np.concatenate((J4,J5,J6),1)

J =np.concatenate( (JM1, JM2),0)
DJ = np.linalg.det(JM1)
IV =np.linalg.inv(JM1)
TJ = np.transpose(JM1)

print("Jacobian Matrix = ")
print(np.around(J,3))
print("Determinant of Jacobian Matrix = ", DJ)
print("Inverse Velocities = ")
print(np.around(IV,3))
print ("Transpose of Jacobian Matrix = ")
print(np.around(TJ))
