# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:02:35 2022

@author: billt
"""

class polynomial(object): 
    
    def __init__(self, myList): #class instance
        self.myList = myList
    
    def order_list(self): # calculate order method
        return(len(self.myList)-1)
    
    def add_list(self,list2): # adding method
        array=[]
        output= ''
        self.list2 = list2
        i=0
        for i in range(0,len(self.myList)): 
            array.append(self.myList[i]+self.list2[i])
            #adding two list of coefficients to 'array'
        for i in range(0,len(array)):
            if i == 0: # no sign if it's very first nomial
                output += (str(array[i])+ "x^"+str(i))# add nomial to 'output' string list
            else:
                if array[i] > 0: #add + infront only if it's positive term
                    output += ("+" + str(array[i]) + "x^"+str(i))
                elif array[i] < 0: # add no sign infront only if it's negative term
                    output += ( str(array[i]) + "x^"+str(i))
                else: # skip the term if coefficient is 0
                    continue
        print("Addition of Two Polynomials is " + output)
    def diff_list(self): # differentiating method
        array = []
        output = ''
        i=0
        for i in range(0,len(self.myList)):
            array.append(self.myList[i] * i)
        for i in range(0,len(self.myList)):
            if i == 0: #remove plus in first term
                    continue
            elif i == 2: #Hard code to remove + sign in very first term
                output += (str((self.myList[i]) * i)+ "x^" + str(i))
            else:
                if self.myList[i] > 0: # diff positive coefficient
                    output += ("+" + str((self.myList[i]) * i)+ "x^" + str(i))
                elif self.myList[i] < 0: # diff negative coefficient
                    output += (str((self.myList[i]) * i)+ "x^" + str(i))
        print("Differentiation of Pa(x) is " + output)
        return polynomial(array)
    def int_list(self,c): #integrating method
#you need to write the 'general' integration method. SO you got original equation back by input the deffrentiated coefficient
        i=1
        for i in range(0, len(self.myList)):
            self.myList[i]=((self.myList[i])/(i+1))
        return polynomial(self.myList)
    def pirnt_poly(self):
        
        output =''
        for i in range(0,len(self.myList)):
            if i == 0: # no sign if it's very first nomial
                output += (str(self.myList[i])+ "x^"+str(i))# add nomial to 'output' string list
            else:
                if self.myList[i] > 0: #add + infront only if it's positive term
                    output += ("+" + str(self.myList[i]) + "x^"+str(i))
                elif self.myList[i] < 0: # add no sign infront only if it's negative term
                    output += ( str(self.myList[i]) + "x^"+str(i))
                else: # skip the term if coefficient is 0
                    continue
        return output

        
        