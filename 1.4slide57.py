# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:52:45 2024

@author: ASUS
"""

def kiem_tra_so(n):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2== 0:
        return 1
    else:
        return 0

so = int(input("Nhập một số: "))
ket_qua = kiem_tra_so(so)
print("Kết quả:", ket_qua)
