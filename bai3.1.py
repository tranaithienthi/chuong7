# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:33:26 2024

@author: ASUS
"""

import random

def khoi_tao_seqA():
    n=random.randint(30, 80)
    seqA=[]
    
    for i in range(n):
        if random.choice([True, False]):
            value=random.randint(-79,39)
        else:
            value=round(random.uniform(-79,39),2)
        seqA.append(value)
    return seqA

seqA = khoi_tao_seqA()
print(seqA)

