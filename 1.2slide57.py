# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:26:33 2024

@author: ASUS
"""

def can_bac(n: int, x: float):
    if n > 0:
        ket_qua = x ** (1/n)
        return ket_qua
    else:
        return "Bậc n phải lớn hơn 0"  

ket_qua = can_bac(2, 3.0)
print(ket_qua)

    