# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:13:48 2021

@author: gnasution
"""

import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
Akomodasi = (20, 116, 61, 58, 64,9 )
Kamar = (1503, 10732, 3653, 5206, 2187, 4781, 523)
Bed = (92579, 16418, 6015, 7832, 2885, 6800, 786)
fig, ax = plt.subplots()
ax.boxplot((Akomodasi, Kamar, Bed), vert=False, showmeans=True, meanline=True,
           labels=('Akomodasi', 'Kamar', 'Bed'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'blue'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

