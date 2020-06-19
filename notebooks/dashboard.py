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

# %% [markdown]
# This demo uses voila to render a notebook to a custom HTML page using gridstack.js for the layout of each output. In the cell metadata you can change the default cell with and height (in grid units between 1 and 12) by specifying.
#  * `grid_row`
#  * `grid_columns`

# %%
import numpy as np
n = 200

x = np.linspace(0.0, 10.0, n)
y = np.cumsum(np.random.randn(n)*10).astype(int)


# %%
import ipywidgets as widgets

# %%
label_selected = widgets.Label(value="Selected: 0")
label_selected

# %% grid_columns=8 grid_rows=4
import numpy as np
from bqplot import pyplot as plt
import bqplot

fig = plt.figure( title='Histogram')
np.random.seed(0)
hist = plt.hist(y, bins=25)
hist.scales['sample'].min = float(y.min())
hist.scales['sample'].max = float(y.max())
display(fig)
fig.layout.width = 'auto'
fig.layout.height = 'auto'
fig.layout.min_height = '300px' # so it shows nicely in the notebook
fig.layout.flex = '1'

# %% grid_columns=12 grid_rows=6
import numpy as np
from bqplot import pyplot as plt
import bqplot

fig = plt.figure( title='Line Chart')
np.random.seed(0)
n = 200
p = plt.plot(x, y)
fig

# %%
fig.layout.width = 'auto'
fig.layout.height = 'auto'
fig.layout.min_height = '300px' # so it shows nicely in the notebook
fig.layout.flex = '1'

# %%
brushintsel = bqplot.interacts.BrushIntervalSelector(scale=p.scales['x'])


# %%
def update_range(*args):
    label_selected.value = "Selected range {}".format(brushintsel.selected)
    mask = (x > brushintsel.selected[0]) & (x < brushintsel.selected[1])
    hist.sample = y[mask]
    
brushintsel.observe(update_range, 'selected')
fig.interaction = brushintsel
