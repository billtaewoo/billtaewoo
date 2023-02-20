# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:47:36 2022

@author: billt
"""
import numpy as np
import math

class HeavenlyBodies(object):
    def __init__(self):
        self.m1 = 6.4185E23 #Mass of Mars
        self.m2 = 1.06E16 #Mass of Phobos
        self.r12 = 9.3373E6 #orbital radius
        self.T = 0.319  #Orbital period days
        self.G = 6.67E-11 #Gravitational Constant
        self.r1_init = np.array([0,0])#initial position of Mars
        self.r2_init = np.array([self.r12,0])#initial position of Phobos
        self.v1_init = np.array([0,0])#initial velocity of Mars
        self.v2_init = np.array([0, math.sqrt((self.G*self.m1)/self.r12)])#initial velocity of Phobos
    
    


    