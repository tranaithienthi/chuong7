# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:37:47 2024

@author: ASUS
"""

#args_
def tinh_tong(*args):
    tong=0
    for i in args:
        tong+=i
    return tong
tong = tinh_tong(1, 2, 3, 4, 5)
print("Tổng là:", tong)

#args_tích
def tinh_tich(*args):
    tich = 1
    for i in args:
        tich *= i
    return tich

tich = tinh_tich(1, 2, 3, 4, 5)
print("Tích là:", tich)

