# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:43:47 2022

@author: billt
"""
import numpy as np
import matplotlib.pyplot as plt

class energy_plot(object):
    def __init__(self):
        self.energyDataArray=[] #array for storing energy data
    
    def read_energy(self):
        self.energyDataArray = np.genfromtxt('energy.txt',dtype=float)
        #This line gets energy from energy.txt and store it as a list in array above
    def display_energy(self):
        self.read_energy()
        x_val = len(self.energyDataArray)
        x = np.linspace(0,x_val,x_val)
        y = self.energyDataArray
        plt.plot(x,y)
        plt.xlabel('seconds')
        plt.ylabel('Energy')
        plt.ylim(0,-10E33)
        plt.show()
        #this function build the energy graph from energydata array.
def main():
    a=energy_plot()
    a.display_energy()

main()
'''remember, make sure energy.txt was not exists or empty before run simulation
and run the simulation. 
energy graph would look giggly but with longer iteration it will refine to 
line.'''