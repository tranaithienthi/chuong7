# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:12:01 2024

@author: ASUS
"""

def kiemtra(x):
    if x % 2 == 0 and x<0:
        return "True"
    else:
        return "Flase" 

so= int(input("Nhập một số:"))
result =kiemtra(so)
print(result)
