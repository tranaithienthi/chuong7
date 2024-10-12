# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:41:05 2024

@author: ASUS
"""

from bai3_1 import khoi_tao_seqA

def thong_ke_so_luong(seqA):
    return len(seqA)

seqA = khoi_tao_seqA()
so_luong = thong_ke_so_luong(seqA)
print(f"Số lượng phần tử trong seqA: {so_luong}")
