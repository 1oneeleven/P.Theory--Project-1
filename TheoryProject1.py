#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:49:28 2024

@author: alialshehhi
"""
#this is my first programming theory git project (portfolio task 1)
#the following code is my FC723 portflio task 1

#ask user for inputs A and B

A = int(input("please enter a number for input A:"))
B = int(input("please enter a number for input B:"))

#Define a function to get calculate the GCD using the Euclidean algorithm 
def CalulateGCD(A, B):
    

    #check if A is larger than B, and reassign A and B if B is larger
    if A<B:
        A, B = B, A
        
        #assign inital value of R as an empty variable

    #If statement to Check if the Input A is negative and print that its invalid
    if A<0:
            print("invalid inputs")
            return 
    
    #If statement to Check if the Input B is negative and print that its invalid
    if B<0: 
            print("invalid inputs")
            return
         
    #create a while loop to calculate GCD and get a remainder using modulus
    while True:
        R = A % B
          
        #print the values of R in the code until the value of R equals to 0
        print(B)
        A, B = B, R
        #Print a message telling the user that their inputs are relaive prime numbers
        if R == 1:
            print ("The inputs of A and B are both Prime Numbers since GCD is:")
        if R == 0:
            break  #end the function 
            
    

    return R
 #calculates the Greatest common divisor of the two inputs from the user
CalulateGCD(A, B)    
        
        

        
        

