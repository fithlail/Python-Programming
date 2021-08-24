# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:41:17 2021

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
hist, bin_edges = np.histogram(Kamar, bins=10)
hist
bin_edges
fig, ax = plt.subplots()
ax.hist(Kamar, bin_edges, cumulative=False)
ax.set_xlabel('Kamar')
ax.set_ylabel('Frequency')
plt.show()