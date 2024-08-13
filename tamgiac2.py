# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:15:49 2024

@author: Nguyen Thi Nhu Ngoc
"""

a= float(input("canh cua tam giac"))
b= float(input("canh cua tam giac"))
c= float(input("canh cua tam giac"))
if a+b > c and a+c > b and b+c > a:
    if a==b==c:
      print("Tam giac deu")
    elif a==b or a==c or b==c:
        if a**2 + b**2== c**2 or a**2 + c**2== b**2 or b**2 + c**2== a**2:
            print("Tam giac vuong can")
        print("Tam giac can")
    elif a**2 + b**2== c**2 or a**2 + c**2== b**2 or b**2 + c**2== a**2:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("khong la tam giac ")
        
        
        
    
    
    