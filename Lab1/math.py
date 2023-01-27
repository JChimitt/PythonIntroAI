# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 03:41:58 2021


"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Enter the operation you would like to perform.")

operation = input("Enter +, -, *, or / for the operation you want: ")
        
output = 0

if operation ==  '+':
        output = num1 + num2
elif operation ==  '-':
        output = num1 - num2
elif operation ==  '*':
        output = num1 * num2
elif operation ==  '/':
        output = num1 / num2
else: print("Invalid input.")

print(num1, operation, num2, ":", output)
"""
@author: Jake
"""

