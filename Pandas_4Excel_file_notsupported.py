#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:32:31 2021

@author: abhinai
"""

import pandas as pd
df_output=pd.read_excel("output.xlsx",engine='openpyxl')
print(df_output)
