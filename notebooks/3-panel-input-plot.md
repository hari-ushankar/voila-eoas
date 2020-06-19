---
jupytext:
  formats: ipynb,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: 'Python 3.7.6 64-bit (''base'': conda)'
  language: python
  name: python37664bitbaseconda1bb8ef0d31da45418649f49cee951ef5
---

```{code-cell} ipython3
from __future__ import print_function
from ipywidgets import GridspecLayout, Button, Layout, interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import numpy as np
import bqplot as bq

def create_expanded_button(description, button_style):
    return Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))

grid = GridspecLayout(5, 5, height='600px')

# inputs
in_box1 = widgets.BoundedFloatText(value=1, min=0, max=100.0, step=0.1, description='a:', disabled=False)
grid[1, 0] = in_box1

in_box2 = widgets.BoundedFloatText(value=1, min=0, max=100.0, step=0.1, description='b:', disabled=False)
grid[2, 0] = in_box2

in_box3 = widgets.BoundedFloatText(value=1, min=0, max=100.0, step=0.1, description='c:', disabled=False)
grid[3, 0] = in_box3

in_dd = widgets.Dropdown(options=['black', 'red', 'blue'], value='black', description='Line colour:', disabled=False)
grid[4, 0] = in_dd

# plot 1
def plot1():
    a = in_box1.value
    b = in_box2.value
    c = in_box3.value
    col = in_dd.value
    def f(t):
        return a*np.exp(b*np.sin(t)) * np.cos(c*np.pi*t)

    da_x = np.arange(0.0, 10.0, 0.01)
    da_y = f(da_x)

    sc_x = bq.LinearScale()
    sc_y = bq.LinearScale()

    ax_x = bq.Axis(scale=sc_x, grid_lines='solid', label='X')
    ax_y = bq.Axis(scale=sc_y, orientation='vertical', tick_format='0.2f',
                grid_lines='solid', label='Y')

    lines = bq.Lines(x=da_x, y=da_y, scales={'x': sc_x, 'y': sc_y},
                 stroke_width=3, colors=[col])

    grid[:, 1:3] = bq.Figure(marks=[lines], axes=[ax_x, ax_y], layout=Layout(width='auto', height='auto'),
                                     fig_margin=dict(top=60, bottom=40, left=40, right=0), title="a*e^(b*sin(t)) * cos(c*pi*t)")

plot1()

# plot 2
def plot2():
    a = in_box1.value
    b = in_box2.value
    c = in_box3.value
    col = in_dd.value
    def f(t):
        return a*np.exp(-t) * np.cos(b*np.pi*t) + c*t

    da_x = np.arange(0.0, 10.0, 0.01)
    da_y = f(da_x)

    sc_x = bq.LinearScale()
    sc_y = bq.LinearScale()

    ax_x = bq.Axis(scale=sc_x, grid_lines='solid', label='X')
    ax_y = bq.Axis(scale=sc_y, orientation='vertical', tick_format='0.2f',
                grid_lines='solid', label='Y')

    lines = bq.Lines(x=da_x, y=da_y, scales={'x': sc_x, 'y': sc_y},
                 stroke_width=3, colors=[col])

    grid[:, 3:5] = bq.Figure(marks=[lines], axes=[ax_x, ax_y], layout=Layout(width='auto', height='auto'),
                                     fig_margin=dict(top=60, bottom=40, left=40, right=0), title="a*e^(-t) * cos(b*pi*t) + c*t")
    
plot2()

# interaction
def handle_input(change):
    plot1()
    plot2()

in_box1.observe(handle_input, names='value')
in_box2.observe(handle_input, names='value')
in_box3.observe(handle_input, names='value')
in_dd.observe(handle_input, names='value')

# grid
grid
```

```{code-cell} ipython3

```
