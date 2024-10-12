# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:04:34 2024

@author: ASUS
"""

import math

def tinh_chuvi_hoac_dientich(*args, **kwargs):
    chu_vi=kwargs.get('chu_vi', None)
    dien_tich=kwargs.get('dien_tich', None)
    hinh = kwargs.get('hinh', None)
    if chu_vi=="Tính chu vi":
        if hinh=='vuong':
            return 4 * args[0] 
        elif hinh == 'chunhat':
            return 2*(args[0] + args[1])
        elif hinh == 'tron':
            return 2*(math.pi)*args[0]
    if dien_tich== "Tính diện tích":
        if hinh=='vuong':
            return args[0]*args[0]
        elif hinh == 'chunhat':
            return args[0]*args[1]
        elif hinh == 'tron':
            return (math.pi)*(args[0]**2)
        
dien_tich_vuong = tinh_chuvi_hoac_dientich(5, dien_tich="Tính diện tích", hinh='vuong')
dien_tich_chu_nhat = tinh_chuvi_hoac_dientich(4, 6, dien_tich="Tính diện tích", hinh='chunhat')
dien_tich_tron = tinh_chuvi_hoac_dientich(3, dien_tich="Tính diện tích", hinh='tron')

chu_vi_vuong = tinh_chuvi_hoac_dientich(5, chu_vi="Tính chu vi", hinh='vuong')
chu_vi_chu_nhat = tinh_chuvi_hoac_dientich(4, 6, chu_vi="Tính chu vi", hinh='chunhat')
chu_vi_tron = tinh_chuvi_hoac_dientich(3, chu_vi="Tính chu vi", hinh='tron')

print("Diện tích hình vuông:", dien_tich_vuong)
print("Diện tích hình chữ nhật:", dien_tich_chu_nhat)
print("Diện tích hình tròn:", dien_tich_tron)

print("Chu vi hình vuông:", chu_vi_vuong)
print("Chu vi hình chữ nhật:", chu_vi_chu_nhat)
print("Chu vi hình tròn:", chu_vi_tron)
