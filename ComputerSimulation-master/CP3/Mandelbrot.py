# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:51:59 2022

@author: billt
"""

import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot(object):
    
    def __init__(self, N,point,xmax,xmin,ymax,ymin,zmax,zmin): #constructor
    
        self.Itr = N
        self.Point = point
        
        self.Xmax = xmax
        self.Xmin = xmin
        
        self.Ymax = ymax
        self.Ymin = ymin
        
        self.Zmax = zmax
        self.Zmin = zmin
        
    def arrays(self): #make arrays
        self.X = np.linspace(self.Xmin, self.Xmax, self.Point)
        self.Y = np.linspace(self.Ymin, self.Ymax, self.Point)
        self.XX,self.YY = np.meshgrid(self.X, self.Y)
        
    def Call_List(self): # Make empty 2D array
        self.List = []
        for i in range(self.Point):
            self.List.append([])
            for j in range(self.Point):
                self.List[i].append(0)
                
    def Mandel(self): #Mandel set
        C = self.XX + 1j*self.YY #Make 2D array of Complex No.
        for i in range(self.Point): 
            for j in range(self.Point): #Pick one complex No. from C
                n = 0
                Z = self.Zmin
                while n<= self.Itr: #exit (Not Mendel)
                    Z = Z * Z + C[i][j]
                    n += 1
                    if abs(Z) > 2:
                        self.List[i][j] = n
                        # print(n)
                        break
                self.List[i][j] = n
                    
        # print(self.List)
    def vis(self): #visual representation
        plt.imshow(self.List)
        plt.colorbar()
        plt.show
        

def main():
    a = Mandelbrot(255, 512, 0.6, -2.025, 1.125, -1.125, 2, 0)
    a.arrays()
    a.Call_List()
    a.Mandel()
    a.vis()
main()