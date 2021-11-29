# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:02:30 2021

@author: mon pc
"""
name1 = input("enter your name, ")
weight1 = int(input("enter your weight, person 1"))
height1 = float(input("enter your height, person 1"))

name2 = input("enter your name, person 2")
weight2 = int(input("enter your weight, person 2"))
height2 = float(input("enter your height, person 2"))

name3 = input("enter your name, person 3")
weight3 = int(input("enter your weight, person 3"))
height3 = float(input("enter your height, person 3"))
def bmi_calculator(name, weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    print("bmi is:")
    print(bmi)
    if bmi < 25:
        return name + ", you are not overweight"
    else:
        return name + ", you are overweight"
result1 = bmi_calculator(name1, weight1, height1)
result2 = bmi_calculator(name2, weight2, height2)
result3 = bmi_calculator(name3, weight3, height3)

print(result1)
print(result2)
print(result3)