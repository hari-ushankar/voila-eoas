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

# Which multiplication table do you want to learn?

In this example notebook we demonstrate how voila can render different Jupyter widgets using [GridspecLayout](https://ipywidgets.readthedocs.io/en/latest/examples/Layout%20Templates.html#Grid-layout)

```{code-cell} ipython3
from ipywidgets import GridspecLayout, Button, BoundedIntText, Valid, Layout, Dropdown

def create_expanded_button(description, button_style):
    return Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))
 
rows = 11
columns = 6

gs = GridspecLayout(rows, columns)

def on_result_change(change):
    row = int(change["owner"].layout.grid_row)
    gs[row, 5].value = gs[0, 0].value * row == change["new"]
    
def on_multipler_change(change):
    for i in range(1, rows):
        gs[i, 0].description = str(change["new"])
        gs[i, 4].max = change["new"] * 10
        gs[i, 4].value = 1
        gs[i, 4].step = change["new"]
        gs[i, 5].value = False

gs[0, 0] = Dropdown(
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    value=2,
)
gs[0, 0].observe(on_multipler_change, names="value")
multiplier = gs[0, 0].value

for i in range(1, rows):
    gs[i, 0] = create_expanded_button(str(multiplier), "")
    gs[i, 1] = create_expanded_button("*", "")
    gs[i, 2] = create_expanded_button(str(i), "info")
    gs[i, 3] = create_expanded_button("=", "")

    gs[i, 4] = BoundedIntText(
        min=0,
        max=multiplier * 10,
        layout=Layout(grid_row=str(i)),
        value=1,
        step=multiplier,
        disabled=False
    )

    gs[i, 5] = Valid(
        value=False,
        description='Valid!',
    )

    gs[i, 4].observe(on_result_change, names='value')

gs
```
