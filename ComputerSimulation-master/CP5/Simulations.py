# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:00:56 2022

@author: billt
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.linalg import norm
from HeavenlyBodies import HeavenlyBodies
from matplotlib.animation import FuncAnimation
HB = HeavenlyBodies()

class Simulations(object):
    
    def motion(self):
        self.R1 = []
        self.R2 = []
        T = HB.T # period
        r1 = HB.r1_init
        r2 = HB.r2_init
        v1 = HB.v1_init
        v2 = HB.v2_init
        m1 = HB.m1
        m2 = HB.m2
        G = HB.G
        t = 0 # time
        while t <= T:
            r12 = r2 - r1
            r21 = r1 - r2
            mag_r12 = norm(r12)
            mag_r21 = norm(r21)
            a1 = (-G*m2/mag_r21**3)*r21
            a2 = (-G*m1/mag_r12**3)*r12
            v1 = v1 + a1
            v2 = v2 + a2
            r1 = r1 + v1
            r2 = r2 + v2
            self.R1.append(r1)
            self.R2.append(r2)
            t += 0.001 #add 15min to t
            
    def animate(self, i):
        #update position
        self.patch1.center = (list(self.R1[i]))
        self.patch2.center = (list(self.R2[i]))
        return self.patch1, self.patch2
    
    def display(self):
        fig = plt.figure()
        ax = plt.axes()
        
        self.patch1 = plt.Circle((self.R1), 0.1, color='b',animated=True)
        self.patch2 = plt.Circle((self.R2), 0.1, color='r',animated=True)
        ax.add_patch(self.patch1)
        ax.add_patch(self.patch2)
        ax.axis('scaled')
        ax.set_xlim(-11,11)
        ax.set_ylim(-11,11)
        
        #animate the plot
        numFrames = len(list(self.R1))
        self.anim = FuncAnimation(fig, self.animate, numFrames, repeat=False, interval=20, blit=True)
        
        plt.show()
        
        

def main():
    a=Simulations()
    a.motion()
    a.display()
    
main()