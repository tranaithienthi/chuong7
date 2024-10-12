# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:48:59 2024

@author: ASUS
"""

import math

def tinh_chu_vi(*args, **kwargs):
    hinh = kwargs.get('hinh', None)
    if hinh=='vuong':
        return 4 * args[0] 
    elif hinh == 'chunhat':
        return 2*(args[0] + args[1])
    elif hinh == 'tron':
        return 2*(math.pi)*args[0]
    
chu_vi_vuong = tinh_chu_vi(5, hinh='vuong')
chu_vi_chu_nhat = tinh_chu_vi(4, 6, hinh='chunhat')
chu_vi_tron = tinh_chu_vi(3, hinh='tron')
print("Chu vi hình vuông:", chu_vi_vuong)
print("Chu vi hình chữ nhật:", chu_vi_chu_nhat)
print("Chu vi hình tròn:", chu_vi_tron)

    