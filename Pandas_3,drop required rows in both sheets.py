#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:25:31 2021

@author: abhinai
"""

import pandas as pd
import re
new=pd.DataFrame({"a":[1,2,3,"abhi"],"b":[7,8,9,"yamu"]})
new=new.iloc[2:,:]
new=new.reset_index(drop=True)
print(new)