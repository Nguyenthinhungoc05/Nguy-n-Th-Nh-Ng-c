# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:17:46 2024

@author: Student
"""

thoigian= input("nhap vao thoi gian hh:mm:ss ")
hh, mm, ss = map(int,thoigian.split (':'))
print("Doi thoi gian ra giay: ", hh*3600 + mm*60 + ss)