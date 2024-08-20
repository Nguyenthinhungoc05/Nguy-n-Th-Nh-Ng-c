# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:15:24 2024

@author: Student
"""
s = "Dai hoc Quoc gia, Khu pho 6, P. Linh Trung, Q. Thu Duc, Tp. HCM"
s1 = s.replace('P. ','').replace('Q. ','').replace('Tp. ','').split(', ') 
for i in s1 :
    print(i)
