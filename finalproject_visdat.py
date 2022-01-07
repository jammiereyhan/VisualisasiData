# -*- coding: utf-8 -*-
"""FinalProject_VisDat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qyYDSpuayQUCE_n9-88QBaXbn_NFgL6U

**Kelompok 14 :**

1. Irawan Prananda Berutu (1301170755)
2. Muhammad Fajar Fadillah (1301180272)
3. Jammie Reyhan Widyanto (1301180077)
"""

# Import Library
import pandas as pd
import numpy as np
# Bokeh Library
import panel as pn
from datetime import date, time, datetime
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row, column, gridplot
from bokeh.models import HoverTool, ColumnDataSource, NumeralTickFormatter, CDSView, GroupFilter

# Inisiasi Dataset dari file csv
df = pd.read_csv('saham.csv')

# Merubah format kolom Date
df['date'] = pd.to_datetime(df['date'])

# Menampilkan dataframe 
df.head()

# Definisi data untuk setiap saham
aa = df[df['symbol'] == 'AAPL']
sh = df[df['symbol'] == 'SHIB']

# Menyimpan data di setiap saham
aaview = ColumnDataSource(aa)
shview = ColumnDataSource(sh)

# Menambahkan Hover
tooltips_volume = [('symbol', '@symbol'), ('volume', '$y{0.2f}'),] 
tooltips_adjHigh = [('symbol', '@symbol'), ('adjHigh', '$y{0.2f}'),] 
tooltips_adjClose = [('symbol', '@symbol'), ('adjClose', '$y{0.2f}')]

# Membuat figur volume
Volume_fig = figure(x_axis_type='datetime',
                    plot_height=500,plot_width=900,
                    x_axis_label='date',y_axis_label='volume',
                    tooltips = tooltips_volume,
                    title='Nilai Volume setiap index saham',)

# Membuat figur adjHigh
adjHigh_fig = figure(x_axis_type='datetime',
                    plot_height=500,plot_width=900,
                    x_axis_label='date',y_axis_label='adjHigh',
                    tooltips = tooltips_adjHigh,
                    title='adjHigh setiap index saham',)

# Membuat figur adjClose
adjClose_fig = figure(x_axis_type='datetime',
                 plot_height=500,plot_width=900,
                 x_axis_label='date',y_axis_label='adjClose',
                 tooltips = tooltips_adjClose,
                 title='adjClose setiap index saham',)

# Visualisasi volume
Volume_fig.circle('date','volume',source=aaview ,color='green', legend_label='AAPL')
Volume_fig.circle('date','volume',source=shview ,color='red', legend_label='SHIB')
Volume_fig.legend.click_policy="hide" # Menyembunyikan legend (sahamnya)
output_notebook()

# Visualisasi adjHigh
adjHigh_fig.circle('date','adjHigh',source=aaview ,color='green', legend_label='AAPL')
adjHigh_fig.circle('date','adjHigh',source=shview ,color='red', legend_label='SHIB')
adjHigh_fig.legend.click_policy="hide" # Menyembunyikan legend (sahamnya)
output_notebook()

# Visualisasi adjClose
adjClose_fig.circle('date','adjClose',source=aaview,  color='green', legend_label='AAPL')
adjClose_fig.circle('date','adjClose',source=shview,  color='red', legend_label='SHIB')
adjClose_fig.legend.click_policy="hide" # Menyembunyikan legend (sahamnya)
output_notebook()

# Panel untuk perpindahan data
Volume_panel = Panel(child=Volume_fig, title='volume')
adjHigh_panel = Panel(child=adjHigh_fig, title='adjHigh')
adjClose_panel = Panel(child=adjClose_fig, title='adjClose')

# Memberikan panel ke tabs
tabs = Tabs(tabs=[Volume_panel, adjHigh_panel, adjClose_panel])

# Output
pn.extension()
pn.pane.Bokeh(tabs)