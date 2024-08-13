# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:58:54 2024

@author: Student
"""

distance=float(input("Nhap do dai doan duong den truong(m):"))
if distance < 300:
    print("duong toi truong qua gan.Thoi! di bo")
elif distance > 1200:
    print("duong den truong qua xa.Thoi! di xe may")
elif distance >= 300 and distance <= 700:
    print(" duong den trung khong xa.Thoi! di xe dap")
else:
    print("khong xac dinh")
    