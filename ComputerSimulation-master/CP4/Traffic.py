# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:17:27 2022

@author: billt
"""
import random

class Traffic(object):
    def __init__(self, NumCell, NumItr, DenCar):
        self.N = NumCell #number of cells
        self.I = NumItr #number of Iteration
        self.D = DenCar #density of car
        
    def generate(self):
        self.C = [] # generate 1D cell
        self.U = [] #empty  update cell
        for i in range(self.N):
            r = random.randint (0, 1)
            self.C.append(r)
        for i in range(self.N):
            a = 0
            self.U.append(a) #make N element 0 filled cell
          
    def update(self):
        new = self.U
        old = self.C
        
        for i in range(0, self.N):
            e = old[i] #ith element
            b = old[(i-1)%self.N] #neighbor behind ith element
            f = old[(i+1)%self.N] #neighbor infront ith element
            for j in range(0, self.N):
                 e2 = new[j] #ith element
                 b2 = new[(j-1)%self.N] #neighbor behind jth element
                 f2 = new[(j+1)%self.N] #neighbor infront jth element
            
            n = 0 #count
            if e == 1: # if ith element filled
                if f == 1: #if car infront
                    e2 = 1 # STAY
                    n += 1 #add count
                elif f == 0: #if no car infront
                    f2 = 1 #fill front cell                   
                    e2 = 0 # vacate the element
                    n += 1 #add count
                    
            elif e == 0: #if ith element empty
                if b == 1: #behind filled
                    e2 = 1 #fill ith element
                    b2 = 0 #vacate behind 
                    n += 1 #add count
                elif b == 0: #if behind empty
                    e2 = 0 #leave ith element 0
                    n += 1
        print(old)
        print(new)
            
             

def main(): #Make a seperate file when ready!
    a = Traffic(10, 10, 10)
    a.generate()
    a.update()
main()
        