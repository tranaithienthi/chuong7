# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:07:24 2024

@author: ASUS
"""

def kiem_tra_doan(n):
    while n<-89 or n>90:
        n=int(input("Nhập lại n: "))
    return n
so=int(input("Nhập một số: "))
ketqua=kiem_tra_doan(so)
