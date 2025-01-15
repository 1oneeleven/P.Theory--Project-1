#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:49:28 2024

@author: alialshehhi
"""
#this is my first programming theory git project (portfolia task 1)
#the following code is my FC723 portflio task 1

#ask user for inputs A and B

A = int(input("please enter a number:"))
B = int(input("please enter a number:"))

#Define a function to get calculate the large number by the smaller number to prove Relative prime numbers

def CalulateGCD(A, B):
    
    #assign inital value of list "GCDlist" as an empty list
    GCDlist = [0]
    #check if A is larger than B 
    if A<B:
        A, B = B, A
        
        #assign inital value of R as an empty variable
        
        #create a while loop to calculate GCD and get a remainder
        while GCDlist:
            R = A % B
            GCDlist.append(R)
            #print the values of R in the code until the value of R equals to 0
            print(R)
            if R==0:
                break
            
            if GCDlist[-1] == 1:
                print ("Your inputs are valid!")
             
            else: 
                GCDlist[-1] != 1
                print ("Error, invalid inputs")
                break
            
            
    

    return R

CalulateGCD(A, B)    
        
        

        
        

