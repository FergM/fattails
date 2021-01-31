# Fat Tails
Python package and Jupyter notebooks for fat-tailed statistics. Inspired by Nassim Taleb's Technical Incerto.

<div>
  <a href="https://pypi.org/project/fattails">
      <img src="https://badge.fury.io/py/fattails.svg" alt="package version"/>
  </a>
</div>

## Content

### Notebooks
See the [notebooks/README.md](./notebooks/) for more detail.

My favourite notebooks so far:
* [Central Limit Theorem: How the sum of Uniform values is Gaussian](./notebooks/NB-22%20-%20Visual%20Central%20Limit%20Theorem.ipynb)
* [S&P500: How geometric average return is impossible](./notebooks/Notebook-11%20-%20Ergodicity%20and%20S%26P500.ipynb)
* [GameStop: January 2021 was not an outlier if you assume Power Law tails.](./notebooks/NB-25%20-%20Survival%20Plot%20-%20Gamestop.ipynb)

### Functions
* `fattails.metrics.mad()`: Calculates mean absolute deviation.
* `fattails.metrics.get_survival_probability()`: Calculate survival probabilities for a given dataset.

Example:
```
$ pip install fattails
$ python

>>> import fattails.metrics as fattails
>>>
>>>
>>> fattails.mad([1,2,3]) # Calculate Mean Absolute Deviation of [1,2,3]
0.6666666666666666
>>>
>>>
>>> fattails.get_survival_probability([1,2,3]) # Get survival probability for each value in your data
0    0.75
1    0.50
2    0.25
Name: survival_probability, dtype: float64
```

### Derivations
* [How much data do I need?](/docs/Notes-02%20-%20Derivation%20-%20How%20much%20data%20do%20I%20need.pdf)

# External Resources
Technical Incerto Book One:
* [PDF on researchers.one](https://researchers.one/articles/20.01.00018)
* [PDF on arxiv.org](https://arxiv.org/abs/2001.10488)
* [Errata](https://www.fooledbyrandomness.com/Errata2020FirstEdition.pdf)

More Links:
* Incerto Reading Club: [Website](http://www.techincertoreadingclub.com/), [GitHub](https://github.com/Technical-Incerto-Reading-Club/code-examples)
* [`StatisticalConsequencesOfFatTails`](https://github.com/MarcosCarreira/StatisticalConsequencesOfFatTails): Code and Links collected by [Marcos Carreira](https://github.com/MarcosCarreira)
