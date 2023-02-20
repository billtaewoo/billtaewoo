# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:11:18 2022

@author: billt
"""

import random
import math

class Rad(object):
    
    def __init__(self, n):
        #create nxn List
        Rad.N = n
        Rad.grid = []
        for i in range(n):
            Rad.grid.append([])
            for j in range(n):#each item in sub list is 0
                Rad.grid[i].append(1)
        print(Rad.grid) #Visual representation of undecayed nuclei
        
    
    def Decay(self, l, dt):# l=lambda, dt= delta t
        Rad.DT = dt # instance variable for dt
        Rad.L = l # instance variable for lambda
        p =  l * dt #probability of decay
        c = 0 #no. of decayed elements
        t = 0 #total time taken
        while c/(Rad.N**2) <= 1/2: #iterate until half of elements are decayed
            t += 1 # time add up everytime decay iterated
            for i in range(0, len(Rad.grid)):
                for j in range(0, len(Rad.grid[0])):
                    rv = random.random() # rv = random number
                    if Rad.grid[i][j] == 1:
                        if rv < p: #Decay if random number is smaller than p
                            Rad.grid[i][j] = 0 #Set decayed element to 0
                            c += 1 # count 1 becasue element decayed
                        else:
                            continue
                    elif Rad.grid[i][j] == 0:
                        continue
        print(Rad.grid) #visual representation of decayed nuclei
        Rad.T = t #time until half-life
        Rad.C = c #count of decayed element
    
    def Count(self): # count of initial and final number of undecayed nuclei
        print("initial number of undecayed element is : "+ str(Rad.N**2))
        print("Final number of undecayed element is : "+ str((Rad.N**2)-Rad.C))
    def HL(self): # value of half life
        print("Simulated value of Half life is : "+ str(Rad.T * Rad.DT) +"min")
    def real_HL(self): #actual value of half life
        RHL = math.log(2)/Rad.L
        print("Actual value of Hald life is : "+ str(RHL))
        
        

def main():
    a = Rad(40)
    a.Decay(0.02775, 0.01)
    a.Count()
    a.HL()
    a.real_HL()
    
main()