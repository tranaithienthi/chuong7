# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:39:57 2024

@author: ASUS
"""

#kwargs
def tinh_tong(**kwargs):
    tong=0
    for i in kwargs:
        tong += kwargs[i]
    return tong
tong = tinh_tong(mot=1, hai=2, ba=3, bon=4, nam=5)
print("Tổng là:", tong)

#kwargs_tich
def tinh_tich(**kwargs):
    tich = 1
    for i in kwargs:
        tich *= kwargs[i]
    return tich

tich = tinh_tich(mot=1, hai=2, ba=3, bon=4, nam=5)
print("Tích là:", tich)
