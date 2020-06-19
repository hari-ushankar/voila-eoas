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

In this example notebook, we demonstrate how voila can render notebooks making use of ipywidget's `@interact`.

```{code-cell} ipython3
from ipywidgets import HBox, VBox, IntSlider, interactive_output
from IPython.display import display

a = IntSlider()
b = IntSlider()

def f(a, b):
    print("{} * {} = {}".format(a, b, a * b))

out = interactive_output(f, { "a": a, "b": b })

display(HBox([VBox([a, b]), out]))
```

```{code-cell} ipython3

```
