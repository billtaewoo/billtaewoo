# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:56:29 2022

@author: billt
"""
from Planets import Beeman
import csv
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Simulation(object):
    def __init__(self, num_of_iterations, dt):
        self.dt = dt #time intervla
        self.num_of_iterations = num_of_iterations #number of iterations
        self.patchList = [] #Storing patches(planets) into this list
        self.objArray = [] #empty list for storing objects from Planets file
        self.G = 6.67*10**(-11) #Gravitational Constant
        self.y_before = np.zeros((4,), dtype=float)#[0,0,0,0]
        self.y_after = np.zeros((4,), dtype=float)#[0,0,0,0]
        self.counter = 0 #counting up for orbital period
        self.period = np.zeros((4,), dtype=float)#[0,0,0,0]
        self.complete_orbit_counter = 0
        '''this is constructor, called when the class Similation is initialised'''
    
    def read_input_data(self):
        
        with open('bodies.csv','r', newline = '') as file:
            reader = list(csv.reader(file))
            
            for i in range(len(reader)):
                obj = Beeman(reader[i][0], float(reader[i][1]), float(reader[i][2]), reader[i][3], float(reader[i][4]))
                self.objArray.append(obj)
#this function is reading a object data from bodies.csv anf import the data in to the Beeman class imported from Planets.py.
#I am using for loop to repeat as much as number of ojects in the system and append the obj into self.objArray.     

    def write_data(self, name, value):   

        with open( name + ".txt", 'a+') as file:
            file.write(str(value)+"\n")

        file.close()
        '''this function if a blueprint of a writing data program that will 
        be used later for storing energy and distance data in upcomming calculation'''
                            
    def update_position(self):
        for i in range(len(self.objArray)):
            self.objArray[i].position = self.objArray[i].position + (self.objArray[i].velocity * self.dt) + ((self.dt**2)/6)*((4 * self.objArray[i].a_t) - self.objArray[i].a_minus_dt)

    def calculate_new_acceleration(self):
        for i in range(len(self.objArray)):
            sigma = 0
            for j in range(len(self.objArray)):
                if i != j:
                    rji = self.objArray[i].position - self.objArray[j].position
                    magnitude_rji = norm(rji)
                    sigma += (self.objArray[j].mass/(magnitude_rji**3))*rji
            self.objArray[i].a_plus_dt = -self.G * sigma
        
    def update_velocity(self):
        for i in range(len(self.objArray)):
            self.objArray[i].velocity = self.objArray[i].velocity + (self.dt/6)*((2*self.objArray[i].a_plus_dt) + (5 * self.objArray[i].a_t) - self.objArray[i].a_minus_dt)
            
    def update_acceleration(self):
        for i in range(len(self.objArray)):
            self.objArray[i].a_minus_dt = self.objArray[i].a_t
            self.objArray[i].a_t = self.objArray[i].a_plus_dt
    '''These functions are basically copy of Beeman integrator. 
    Functionname is very straight forward.
    Things to notice is that I used the for loop to call every planet objects 
    and run the simulation.'''
            
    def process_iteration(self):    
        self.store_y_before_update()
        self.update_position()
        self.store_y_after_update()
        self.checking_y()
        self.write_data('distance_diff',self.distance_between_mars_and_satellite())
        self.calculate_new_acceleration()
        self.update_velocity()
        self.update_acceleration()
        self.write_data('energy',self.calculate_total_energy())
    '''process iteration is iteration step I set for every repeatition.
    This is important part. very important. function names are very straight
    -forward so I will skip the further expalnation.'''
       
    def animate_orbit(self, i):
        self.process_iteration()

        for i in range(len(self.objArray)):
            self.patchList[i].center = self.objArray[i].position
        return self.patchList
    '''animation part which makes an iteration process. 
    This is the alpha and omega of the simulation. very important.'''
    def display_orbit(self):
        fig = plt.figure()
        ax = plt.axes()
        
        for i in range(len(self.objArray)):
            if self.objArray[i].name != "sun":
                self.patchList.append(plt.Circle(self.objArray[i].position, self.objArray[i].radius*1000, color = self.objArray[i].colour, label=self.objArray[i].name, animated = True))
            else:
                self.patchList.append(plt.Circle(self.objArray[i].position, self.objArray[3].radius*7000, color = self.objArray[i].colour, label=self.objArray[i].name, animated = True))

            
        for i in range(len(self.objArray)):
            ax.add_patch(self.patchList[i])
        
        ax.axis('scaled')
        ax.set_xlim(-(1E12),1E12)
        ax.set_ylim(-(1E12),1E12)
        
        self.anim = FuncAnimation(fig, self.animate_orbit, frames = self.num_of_iterations, repeat=False, interval = 1, blit=True)
        
        plt.legend()
        plt.show()
        '''this function is for animation. radius of sun is too big if it is in same scale as IRL, so size of sun is limited by if statement.'''
    def calculate_total_potential_energy(self):
        sigma = 0
        for i in range(len(self.objArray)):
            for j in range(len(self.objArray)):
                if i != j:
                    rij = self.objArray[j].position - self.objArray[i].position
                    sigma += (self.G * self.objArray[i].mass * self.objArray[j].mass)/norm(rij)
        E = -0.5 * sigma
        return E
    '''This function calculate the total potential energy following the equation 
    given in the project book. total potential energy is returned for later calculation'''
    
    def calculate_total_kinetic_energy(self):
        E = 0
        for i in range(len(self.objArray)):
            E += self.objArray[i].kinetic_energy
        return E
    '''This function collects the kinetic energy of each bodies and take a sum of them. 
total kinetic energy is returned for late calculation'''    
    def calculate_total_energy(self):
        E = 0.0

        k = self.calculate_total_kinetic_energy()
        u = self.calculate_total_potential_energy()
        # sum of total kinetic and potential energy
        E = k + u
        return E
    '''This function gets the energy values from two previous energy calculating functions and take a sum.
    sum of two energy is now become a total energy of system and it will return for later use'''
    def store_y_before_update(self):
        for i in range(1,5):
            self.y_before[i-1] = self.objArray[i].position[1]  
    def store_y_after_update(self):
        for i in range(1,5):
            self.y_after[i-1] = self.objArray[i].position[1]  
        self.counter += 1
    '''This two functions are for storing position of planets previous and after
    update of position. self.counter is used to count time in later'''
    def checking_y(self):
        for i in range(4):
            if self.period[i] == 0:
                if (self.y_before[i]<0) and (self.y_after[i]>0):
                    period = (self.counter * self.dt)/3.154E7
                    self.period[i]=period
                    self.complete_orbit_counter += 1
                else:
                    continue
            elif self.complete_orbit_counter == 4:
                self.write_data('period', self.period)
                self.complete_orbit_counter += 1
    '''These three function gets position before update and after update and compare'''
    '''especially in checking_y, it runs a loop until all four planets have a 
    change in y value from negative to positive. To know all four orbit is complete,
    self.complete_orbit_counter is counted 1 up as one planet finishes one orbit.
    if all 4 counts are up, period is written as a name period in external file. and 
    to prevent the infinite write, set +1 to counter to make total count 5 to prevent 
    redundant write.'''
    '''orbital period is calculated by multiplication of dt and self.counter, since
    this is synchronised with process of iteration for orbital simulation.
    period is divided by 3.154E7 to convert second to year'''
                    
    def distance_between_mars_and_satellite(self):
            D = norm(self.objArray[4].position-self.objArray[5].position)
            return D
'''this function collects the position of the mars and satellite and subtracted it.
because the values are in form of vector, normalisation takes a role to find magnitude of distance
'''
def main():
    a = Simulation(12000, 18000)
    a.read_input_data()
    a.display_orbit()
    
    
main()
'''There is few CAUTION to know before run this file.
1. Please delete the distance_diff.txt, energy.txt, period.txt before run.
This simulator doesn't include overwrite system. So please erase the files if 
you like to re run the simulations.

2. Sometimes animation may stop or spits the error out, I do not know the
specific reason, yet it is fixed when I reset the kernel. Please reset the
kernel if similar problem is occured.

3. I set number of iteration and dt as 12000, 18000. dt is 'second'.

4. **very important** Orbital period is stored in period.txt. It is stroed in
list. I didn't have much time to write the code to elaborate which value is 
which. But I set the guidance on this line
-----------------------------------------------------------------------------
period.txt

[period of mercury, period of venus, period of earth, period of mars]

(every value in the period is in Earth Year)
-----------------------------------------------------------------------------


'''
