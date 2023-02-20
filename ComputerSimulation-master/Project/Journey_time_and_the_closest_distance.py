# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:02:24 2022

@author: billt
"""
import numpy as np
class Journey_time_and_the_closest_distance(object):
    def __init__(self,dt):
        self.dt = dt #dt
        self.distance_difference_array = [] #empty arrat for storing distance data
    def read_distance_difference(self):
        self.distance_difference_array = np.genfromtxt('distance_diff.txt',dtype=float)
        #this line read the data from distance_diff.txt and store it in array as list
    def find_journey_time_of_satellite(self):
        self.read_distance_difference()
        Dmin = np.min(self.distance_difference_array)#Find minimum value from array
        Dmin_km = Dmin/1000 #make it in km
        Dindx = np.argmin(self.distance_difference_array)
        journey_time = (Dindx) * self.dt
        per_year = journey_time/31536000
        print('The closest distance reached is ', float(Dmin_km),'km')
        print('Time taken by the satellite to the closest point to the Mars is ', float(per_year), 'year')

def main():
    a = Journey_time_and_the_closest_distance(18000)
    a.find_journey_time_of_satellite()
main()
        
'''This whole file is built for finding the closest distance between
satellite and mars, and show how long does it takes to reach that distance.
Important Things to notice before running this file:
    
1. Check is distance_diff.txt is exists. It gets data from the file.

2. If you look at this line before running Simulation_final.py,
run Simulation.py first. But becareful, as also mentioned in simulation
file, delete the distance_diff.txt first before running simulation.
This is becasue file is not overwritten when running a new simulation.

3. Becasue this file is standalone file, you have to manually type the
dt to match the dt in simulation file. Reason why I separate the file 
is error is generated becasue all code runs simultaneously in the Spyder,
eventhough the codes must run step by step for my case. Sorry for 
inconvenience.'''