# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:29:59 2022

@author: billt
"""

from numpy.polynomial import Polynomial

class Poly(object): #Class Name
    
    def __init__(self, a): #constructor : a = coeff poly initial set
        Poly.list = a # instance variable
        # print(Poly.list)
    def O(self): #Order of Pa
        print("Order is " + str(len(Poly.list)-1)) #print the order of the equation: number of terms -1
    
    def Add(self, b): #Adding two polynimials : b = coeff of poly want to add
        Poly.list2 = b #instance variable
        Sum = [] #Sum List
        Sum = [a + b for a, b in zip(Poly.list, Poly.list2)] # Sum of two list
        p1 = Polynomial(Sum) # make list 'Sum' into Polynomial form
        print(p1)
    
    def Der(self):#first derivative of polynomial
        Der=[] #Deriv List
        for i in range(1, len(Poly.list)): # Start from 1 for skip constant
                Der.append(Poly.list[i] * i) # append derivated coefficient to the empty list Der
        p2 = Polynomial(Der) # make list 'Der' into polynomial form
        print(p2)
    
    def Int(self,c,con):#Integral of polynomial : c = coefficient of poly want to Int, con= constant given
        Int=[] #Int List
        Int.append(con) #Add given constant infront
        for i in range(0, len(c)): 
            Int.append((c[i])/(i+1)) 
        p3 = Polynomial(Int)
        print(p3)

def main():
    eq = Poly([2,0,4,-1,0,6])
    eq.O()
    eq.Add([-1,-3,0,4.5,0,0])
    eq.Der()
    eq.Int([0, 8, -3, 0, 30], 2)


main()
            