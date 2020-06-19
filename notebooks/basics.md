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

# So easy, *voilà*!

In this example notebook, we demonstrate how voila can render Jupyter notebooks with interactions requiring a roundtrip to the kernel.

+++

## Jupyter Widgets

```{code-cell} ipython3
import ipywidgets as widgets

slider = widgets.FloatSlider(description='$x$', value=4)
text = widgets.FloatText(disabled=True, description='$x^2$')

def compute(*ignore):
    text.value = str(slider.value ** 2)

slider.observe(compute, 'value')

widgets.VBox([slider, text])
```

## Basic outputs of code cells

```{code-cell} ipython3
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris
```

```{code-cell} ipython3

```
