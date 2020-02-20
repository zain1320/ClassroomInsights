# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:14:58 2020

@author: AS
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

random.seed(7)

df = pd.DataFrame(np.random.randint(0,10,size=[8,5]), 
                  index=pd.date_range("2020-2-19 8:00:00",periods=8,freq="10min",name="time"), 
                  columns=['confused','focusing','thinking','exciting','sleepy'])
df=df.reset_index()

plt.figure(figsize=(16, 12))

ax1=sns.lineplot(x='time',y='confused',data=df,label='confused')
ax1.lines[0].set_linestyle("--")

ax2=sns.lineplot(x='time',y='focusing',data=df,label='focusing')
ax2.lines[1].set_linestyle("-.")

sns.lineplot(x='time',y='thinking',data=df,label='thinking')
ax2.lines[2].set_linestyle(":")

sns.lineplot(x='time',y='exciting',data=df,label='exciting')
ax2.lines[3].set_linestyle("")

sns.lineplot(x='time',y='sleepy',data=df,label='sleepy')
ax2.lines[4].set_linestyle("-.")
