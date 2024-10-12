# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:48:21 2024

@author: ASUS
"""

from bai3_1 import khoi_tao_seqA
def sap_xep_tang_dan(seqA):
    seqB = sorted(seqA)
    return seqB

seqA = khoi_tao_seqA() 
seqB = sap_xep_tang_dan(seqA)
print("Dãy seqA:", seqA)
print("Dãy seqB (sắp xếp tăng dần):", seqB)