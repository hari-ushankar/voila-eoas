# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from __future__ import print_function
from ipywidgets import GridspecLayout, Button, Layout, interact, interactive, fixed, interact_manual
from bqplot import pyplot as plt
from pathlib import Path
import ipywidgets as widgets
import numpy as np
import bqplot as bq
import pandas as pd
import json
import os

with open(os.path.join('modtran_data', 'toc_files.json'),'r') as infile:
    co2_dict = json.load(infile)
    
def get_df(dir_path):
    pqfile = 'modtran_data' / dir_path / 'rad_spectrum.pq'
    df = pd.read_parquet(pqfile)
    return df

grid = GridspecLayout(4, 2, width='1200px', height='600px')

# inputs
in_dd1 = widgets.Dropdown(options=['0', '10', '100', '1000'], value='0', description='CO2 Conc.:', disabled=False)
grid[1, 0] = in_dd1

in_dd2 = widgets.Dropdown(options=['wavlen_um'], value='wavlen_um', description='X:', disabled=False)
grid[2, 0] = in_dd2

in_dd3 = widgets.Dropdown(options=['total_trans', 'total_radiance_mum'], value='total_trans', description='Y:', disabled=False)
grid[3, 0] = in_dd3

# plot
def plot():
    co2_conc = in_dd1.value
    key_x = in_dd2.value
    key_y = in_dd3.value
    
    dir_name = Path(co2_dict[co2_conc])
    df = get_df(dir_name)

    sc_x = bq.LinearScale(min=5, max=25)
    sc_y = bq.LinearScale()
    
    da_x = df[key_x]
    da_y = df[key_y]
    
    ax_x = bq.Axis(scale=sc_x, grid_lines='solid', label=key_x)
    ax_y = bq.Axis(scale=sc_y, orientation='vertical', label=key_y)
    
    lines = bq.Lines(x=da_x, y=da_y, scales={'x': sc_x, 'y': sc_y},
             stroke_width=3, colors=['blue'])
    
    #ax.plot('wavlen_um','total_trans',data=df)
    #ax.set_title(key)
    #ax.set_xlim([5,25])
    grid[:, 1:2] = bq.Figure(marks=[lines], axes=[ax_x, ax_y], layout=Layout(width='auto', height='auto'),
                             fig_margin=dict(top=60, bottom=40, left=40, right=0), 
                             title=key_x + ' vs ' + key_y + ' with CO2 conc. = ' + co2_conc)
plot()

# interaction
def handle_input(change):
    plot()

in_dd1.observe(handle_input, names='value')
in_dd2.observe(handle_input, names='value')
in_dd3.observe(handle_input, names='value')

# grid
grid
