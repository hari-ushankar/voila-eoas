---
jupytext:
  formats: ipynb,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

This demo uses voila to render a notebook to a custom HTML page using gridstack.js for the layout of each output. In the cell metadata you can change the default cell with and height (in grid units between 1 and 12) by specifying.
 * `grid_row`
 * `grid_columns`

```{code-cell} ipython3
import numpy as np
n = 200

x = np.linspace(0.0, 10.0, n)
y = np.cumsum(np.random.randn(n)*10).astype(int)
```

```{code-cell} ipython3
import ipywidgets as widgets
```

```{code-cell} ipython3
label_selected = widgets.Label(value="Selected: 0")
label_selected
```

```{code-cell} ipython3
:grid_columns: 8
:grid_rows: 4

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
```

```{code-cell} ipython3
:grid_columns: 12
:grid_rows: 6

import numpy as np
from bqplot import pyplot as plt
import bqplot

fig = plt.figure( title='Line Chart')
np.random.seed(0)
n = 200
p = plt.plot(x, y)
fig
```

```{code-cell} ipython3
fig.layout.width = 'auto'
fig.layout.height = 'auto'
fig.layout.min_height = '300px' # so it shows nicely in the notebook
fig.layout.flex = '1'
```

```{code-cell} ipython3
brushintsel = bqplot.interacts.BrushIntervalSelector(scale=p.scales['x'])
```

```{code-cell} ipython3
def update_range(*args):
    label_selected.value = "Selected range {}".format(brushintsel.selected)
    mask = (x > brushintsel.selected[0]) & (x < brushintsel.selected[1])
    hist.sample = y[mask]
    
brushintsel.observe(update_range, 'selected')
fig.interaction = brushintsel
```
