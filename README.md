# Sample Voila Notebooks

## Installation

1. To install the necessary dependencies, run:
```
cd voila-eoas
conda env create -f environment.yml
```

2. Open a terminal, and run the following the following in the `voila-eoas` folder.
This will open a tab in your browser showing the directory structure of voila-server.
Click one of the notebooks (.ipynb files) to run it.
```
voila
```

3. To work on these notebooks, open a second terminal, cd into the voila-eoas directory,
and run the following. This will open a new tab that acts like an IDE for python
code and jupyter books. You can open one of the existing books or create a new one
from here.
```
jupyter lab
```

## Open Issues
- LaTeX not loading: https://github.com/voila-dashboards/voila/issues/516
