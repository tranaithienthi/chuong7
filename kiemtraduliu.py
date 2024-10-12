# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:25:05 2024

@author: ASUS
"""

def kiem_tra_kieu_du_lieu(danh_sach):
    ket_qua = []
    for phan_tu in danh_sach:
        if isinstance(phan_tu, str):
            ket_qua.append(f"'{phan_tu}' là kiểu dữ liệu chuỗi")
        elif isinstance(phan_tu, bool):
            ket_qua.append(f"{phan_tu} là kiểu dữ liệu Boolean")
        elif isinstance(phan_tu, int):
            ket_qua.append(f"{phan_tu} là kiểu dữ liệu số nguyên")
        elif isinstance(phan_tu, float):
            ket_qua.append(f"{phan_tu} là kiểu dữ liệu số thực")
        elif isinstance(phan_tu, complex):
            ket_qua.append(f"{phan_tu} là kiểu dữ liệu số phức")
        else:
            ket_qua.append(f"{phan_tu} là kiểu dữ liệu khác")
    return ket_qua

danh_sach = [123, "hello", 3.14, True, 1+2j, False]
ket_qua = kiem_tra_kieu_du_lieu(danh_sach)
for dong in ket_qua:
    print(dong)
