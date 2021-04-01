#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:20:39 2021

@author: abhinai
"""
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
    
#     for i in range(2,n+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(5)

# import pandas as pd
# df=pd.DataFrame({"a":[1,2,3,4,5],
#                  "b":[6,7,8,9,10],
#                  "c":["ab","bc","cd","ef","ij"]})
# # print(df)

# df["d"]=df["a"].astype(str)+"_"+df["b"].astype(str)
# print(df)


import pandas as pd
df=pd.DataFrame({"height":[1,2,3,4,5]})
print(df)

new=[]

for i in range(0,len(df["height"])):
    if i<3:
        new.append("low")
    else:
        new.append("high")
        
c=new
df["name"]=c
print(df)
        



    