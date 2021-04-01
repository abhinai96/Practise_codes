#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:53:46 2021

@author: abhinai
"""

import pandas as pd
import re
new=pd.DataFrame({"a":["an d","new","old","abhi"],"b":["her","his","him","yamu"]})
new["a"]= re.sub(r' ','',new["a"])





# >>> df['BrandName'].replace(['ABC', 'AB'], 'A')
