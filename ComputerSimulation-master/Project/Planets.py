# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import norm

class Beeman(object):
    def __init__(self, name, m, radius_of_orbit, colour, radius):
        self.name = name 
        self.mass = m
        self.orbital_radius = radius_of_orbit
        self.colour = colour
        self.radius = radius
        self.G = 6.673*(10**(-11))
        self.velocity = np.array([0,0])
        if self.name.lower() == "satellite":
            # optimal velocity around escape velocity of Earth & optimal velocity of sun (Earth< v < Sun)
            self.velocity = np.array([0,35190])
        elif (self.name.lower() != "sun") & (self.name.lower() != "satellite"):
            self.velocity = np.array([0,np.sqrt((self.G*1.989E30)/self.orbital_radius)])
        self.position = np.array([self.orbital_radius,0])
        self.a_minus_dt = np.array([0,0])
        self.a_t = np.array([0,0])
        self.a_plus_dt = np.array([0,0])
        self.kinetic_energy = 0.5 * self.mass * (norm(self.velocity) **2)
        '''This is class object where recieve the data from bodies.csv, processed
        through Simulation_final.py. It gets name, mass, orbital radius, colour,
        radius from data. And this class also function as storing position and
        velocity and acceleration as time goes through. Furthermore, it processes
        the kinetic energy of each bodies and store them'''
        
        
        
        
        
