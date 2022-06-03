"""
Filename: IK_SMMV.py
Created on Wednesday 25/05/2022
Title: Inverse Kinematics of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
a1 = 10mm
a2 = 40mm
a3 = 40mm
X = 62.831mm
Y = 62.831mm 
Z = 20.226mm
"""

import numpy as np
import math

Th1 = np.arctan(float(62.831)/float(62.831))*180.0/np.pi
r1 = math.sqrt((float(62.831)**2)+(float(62.831)**2))
r2 = float(20.226) - float(10)
r3 = math.sqrt((r1**2)+(r2**2))
d3 = math.sqrt((r3**2)-(float(40)**2)) - float(40)
Pi1 = np.arctan((float(40)+float(40))/float(40))*180.0/np.pi
Pi2 = np.arctan(r2/r1)*180.0/np.pi
Th2 =   Pi1 + Pi2 -90.0

print("THETA 1 = ", np.around (Th1,3))
print("THETA 2 = ", np.around (Th2,3))
print("d3 =",  np.around (d3,3))