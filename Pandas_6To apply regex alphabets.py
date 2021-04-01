#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:29:58 2021

@author: abhinai
"""

import pandas as pd
import re
new=pd.DataFrame({"a":[1,2,3,"abhi"],"b":[7,8,9,"yamu"]})


new=new.loc[new.a.astype(str).str.match(r'\d+')]

print(new)

print(type(new))
