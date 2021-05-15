# Fat Tails
Python package and Jupyter notebooks for fat-tailed statistics. Inspired by Nassim Taleb's Technical Incerto.

[![PyPI](https://img.shields.io/pypi/v/fattails)](https://pypi.org/project/fattails/)
[![PyPI - License](https://img.shields.io/pypi/l/fattails)](https://github.com/FergM/fattails/blob/main/LICENSE)

## Content

### Notebooks
See the [notebooks/README.md](https://github.com/FergM/fattails/blob/main/notebooks/README.md) for more detail.

My favourite notebooks so far:
* [Central Limit Theorem: How the sum of Uniform values is Gaussian](https://github.com/FergM/fattails/blob/main/notebooks/NB-22%20-%20Visual%20Central%20Limit%20Theorem.ipynb)
* [S&P500: How geometric average return is impossible](https://github.com/FergM/fattails/blob/main/notebooks/Notebook-11%20-%20Ergodicity%20and%20S%26P500.ipynb)
* [GameStop: January 2021 was not an outlier if you assume Power Law tails.](https://github.com/FergM/fattails/blob/main/notebooks/NB-25%20-%20Survival%20Plot%20-%20Gamestop.ipynb)
* [Tail Alpha: How to estimate the mean of a power law](https://github.com/FergM/fattails/blob/main/notebooks/NB34%20-%20Tail%20Alpha%20Distribution.ipynb)


### Functions
Quick Access:
* [`fattails.mad()`](https://github.com/FergM/fattails/blob/main/fattails/metrics.py#L7): Calculates mean absolute deviation.
* [`fattails.plot_MS_moments()`](https://github.com/FergM/fattails/blob/main/fattails/express.py#L7): Plots the cumulative max/sum ratio of moments 1 to 4.

Other:
* [`fattails.metrics.get_survival_probability()`](https://github.com/FergM/fattails/blob/main/fattails/metrics.py#L35): Calculate survival probabilities for a given dataset.
* [`fattails.metrics.calculate_moments()`](https://github.com/FergM/fattails/blob/main/fattails/metrics.py#L94): Generate dataframe with the chosen moments for each datapoint
* [`fattails.metrics.max_over_sum()`](https://github.com/FergM/fattails/blob/main/fattails/metrics.py#L132): Calculate the cumulative max/sum ratio

Example:
```
$ pip install fattails
$ python

>>> import fattails
>>>
>>>
>>> fattails.mad([1,2,3]) # Calculate Mean Absolute Deviation of [1,2,3]
0.6666666666666666
>>>
>>>
>>> fattails.metrics.get_survival_probability([1,2,3]) # Get survival probability for each value in your data
0    0.75
1    0.50
2    0.25
Name: survival_probability, dtype: float64
```

### Derivations
* [How much data do I need?](https://github.com/FergM/fattails/blob/main/docs/Notes-02%20-%20Derivation%20-%20How%20much%20data%20do%20I%20need.pdf)

## Contact
Jump straight to [discussions](https://github.com/FergM/fattails/discussions) or check out the [contributing guidelines](https://github.com/FergM/fattails/blob/main/docs/CONTRIBUTING.md). Feedback and suggestions are really appreciated!

### Contributors
Special thanks to:
* Daniel Reti: [github.com/drettt](https://github.com/drettt)

# External Resources
Technical Incerto Book One:
* Free PDF: [researchers.one](https://researchers.one/articles/20.01.00018), [arxiv.org](https://arxiv.org/abs/2001.10488)
* Errata: [fooledbyrandomness.com](https://www.fooledbyrandomness.com/Errata2020FirstEdition.pdf)

More Links:
* Incerto Reading Club: [Website](http://www.techincertoreadingclub.com/), [GitHub](https://github.com/Technical-Incerto-Reading-Club/code-examples)
* [`StatisticalConsequencesOfFatTails`](https://github.com/MarcosCarreira/StatisticalConsequencesOfFatTails): Code and Links collected by [Marcos Carreira](https://github.com/MarcosCarreira)
