# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:40:29 2021

@author: gnasution
"""

import datapane as dp
dp.login(token='cf6ee0bcb0c4350bbb1edaaa6f31134f965276a6')
import folium
import pandas as pd

m = folium.Map(location=[-7.2459717, 112.7378266])

data = pd.read_csv('https://raw.githubusercontent.com/rizkysifaul/PyCon_ID_2020/main/Maps%20of%20Surabaya/Surabaya_Full_of_Data.csv')

report = dp.Report(dp.Plot(m),
                   dp.Table(data, caption="Data Surabaya Neighborhood on 2015")
                   )

report.publish(name='folium_map_surabaya')
