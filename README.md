# Fat Tails
Fat Tailed Statistics package and Jupyter notebooks. Inspired by Nassim Taleb's Technical Incerto.

## Content

### Notebooks
You can find a list of notebooks in [docs/notebooks.md](./docs/notebooks.md).

My favourite notebooks so far:
* [Central Limit Theorem: How the sum of Uniform values is Gaussian](./notebooks/NB-22%20-%20Visual%20Central%20Limit%20Theorem.ipynb)
* [S&P500: How geometric average return is impossible](./notebooks/Notebook-11%20-%20Ergodicity%20and%20S%26P500.ipynb)

### Functions
* `fattails.metrics.mad()`: Calculates mean absolute deviation.

Example:
```
$ pip install fattails
$ python

>>> import fattails
>>> from fattails.metrics import mad
>>> mad([1,2,3]) # Calculate Mean Absolute Deviation of [1,2,3]
0.6666666666666666
```

### Derivations
* [How much data do I need?](/docs/Notes-02%20-%20Derivation%20-%20How%20much%20data%20do%20I%20need.pdf)

# External Resources
E-Book:
* [Vol 1 of the Technical Incerto](https://researchers.one/articles/20.01.00018)
    * [Errata](https://www.fooledbyrandomness.com/Errata2020FirstEdition.pdf)

More Links:
* [StatisticalConsequencesOfFatTails](https://github.com/MarcosCarreira/StatisticalConsequencesOfFatTails) collaborative links to code and commentaries.
