# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:51:39 2024

@author: ASUS
"""

from bai3_1 import khoi_tao_seqA
def tinh_trung_binh(seqA):
    trung_binh = sum(seqA) / len(seqA)
    return trung_binh

seqA = khoi_tao_seqA()
trung_binh = tinh_trung_binh(seqA)
print(f"Trung bình các phần tử trong seqA: {trung_binh:.2f}")
