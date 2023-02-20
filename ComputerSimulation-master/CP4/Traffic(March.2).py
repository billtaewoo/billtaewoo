# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:17:27 2022

@author: billt
"""
import numpy as np
import matplotlib.pyplot as plt

class Traffic(object):
    def __init__(self, NumCell, NumItr, DenCar):
        self.N = NumCell #number of cells
        self.I = NumItr #number of Iteration
        self.D = DenCar #density of car
        
    def generate(self):
        self.C = np.zeros((self.I+1,self.N)) # row of I x N

        for i in range(self.N):
            if np.random.rand() < self.D:
                self.C[0,i] = 1
            else:
                self.C[0,i] = 0
        print(self.C)
        
        
          
    def update(self):
        road = list(self.C[0,:])
        self.CN = np.count_nonzero(road) #total number of car in the self.C
        print("no.car",self.CN)
        # print("\n road, ", road)
        n = 0 #count of itr
        
        while n < self.I:
            # print("\n self C", self.C)
            for i in range(0, self.N):
                e = road[i] #ith element
                b = road[(i-1)%self.N] #neighbor behind ith element
                f = road[(i+1)%self.N] #neighbor infront ith element
                m = 0
                
                if e == 1: # if ith element filled
                    if f == 1: #if car infront
                        road[i] = 1
                        road[(i+1)%self.N] = 1 #stay
                        # e = 1
                        
                       
                    elif f == 0: #if no car infront
                        road[(i+1)%self.N] = 1
                        road[i] = 0
                        # f = 1
                        # e = 0
                        m += 1 # 1 car moved
                    # elif b == 1:
                    #     b = 1
                        
                    elif b == 1:
                        road[(i-1)%self.N] = 1
                        road[i] = 1 #stay
                
                elif e == 0: #if ith element empty
                    if b == 1: #behind filled
                        # road[(i-1)%self.N] = 0 #behind car fill the front
                        e = 1
                        b = 0
                        m += 1 # car moved
                    
                    elif b == 0: #if behind empty
                        e = 0 #nothing happened
                # print("m:",m)
            # print("m:",m)
            self.move = m
            self.C[n+1,:] = list(road)
            n += 1
        # print("m:",m)
        # print(n)
        print(self.C)
        
        
    def AverageVelocity(self):
        avg=self.move/self.CN
        print(avg)
       

    def animate(self):
        plt.imshow(self.C[:,1:-1], interpolation = 'none', origin='lower')
        plt.gca().invert_yaxis()
        plt.show()
        

def main(): #Make a seperate file when ready!
    a = Traffic(10, 10, 0.5)
    a.generate()
    a.update()
    a.AverageVelocity()
    a.animate()
main()
        