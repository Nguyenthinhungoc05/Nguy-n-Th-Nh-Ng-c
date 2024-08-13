# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:01:17 2024

@author: Student
"""
so_km = float(input("so km da di= "))
a=  39000 + 60000 + (so_km - 8 )*10000
if so_km <=1:
    print("Tong tien= ", so_km * 20000)
elif 1< so_km <= 3:
    print("Tong tien= ",20000 + (so_km -1)* 13000)
elif 3< so_km <= 8:
    print("Tong tien= ", 39000 + (so_km -3)*12000 )
else:
    print("Tong tien= ", 39000 + 60000 + (so_km - 8 )*10000)
if  a > 100000:
    print("Tong tien sau khi giam= ",a - (a * 8/100))

    

    