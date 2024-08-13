# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:00:24 2024

@author: DELL
"""

import random
cacluachon = ("keo", "bua","bao")
nguoi = input("ban chon gì? (keo,bua,bao)")
may = random.choice(cacluachon)
print(f"ban chon: {nguoi}")
print(f"may chon: {may}")
if nguoi == may:
    print("Hoa")
elif nguoi == "keo" and may == "bao" or \
     nguoi == "bua" and may == "keo" or \
     nguoi =="bao" and may == "bua":
         print("Ban thang")
else:
    print("Ban thang")
            
        


