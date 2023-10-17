# Fat Tails
Notes and Code for fat-tailed statistics. Inspired by Nassim Taleb's Technical Incerto.

[![PyPI - License](https://img.shields.io/pypi/l/fattails)](https://github.com/FergM/fattails/blob/main/LICENSE)

# Table of Contents
* 1. [Blog](./blog)
* 2. [Python Notebooks](#notebooks)
* 3. [External Resources](#external-resources)
* [Other](#other-notes)

### Blog
See [fattails/blog/](./blog)
* 2023-10: I am drafting some articles about Entropy as used in information theory.

### Notebooks
See the [notebooks/README.md](https://github.com/FergM/fattails/blob/main/notebooks/README.md) for more detail.

My favourite notebooks so far:
* [Central Limit Theorem: How the sum of Uniform values is Gaussian](https://github.com/FergM/fattails/blob/main/notebooks/NB-22%20-%20Visual%20Central%20Limit%20Theorem.ipynb)
* [S&P500: How geometric average return is impossible](https://github.com/FergM/fattails/blob/main/notebooks/Notebook-11%20-%20Ergodicity%20and%20S%26P500.ipynb)
* [GameStop: January 2021 was not an outlier if you assume Power Law tails.](https://github.com/FergM/fattails/blob/main/notebooks/NB-25%20-%20Survival%20Plot%20-%20Gamestop.ipynb)
* [Tail Alpha: How to estimate the mean of a power law](https://github.com/FergM/fattails/blob/main/notebooks/NB34%20-%20Tail%20Alpha%20Distribution.ipynb)

### External Resources
Technical Incerto Book One:
* Free PDF: [researchers.one](https://researchers.one/articles/20.01.00018), [arxiv.org](https://arxiv.org/abs/2001.10488)
* Errata: [fooledbyrandomness.com](https://www.fooledbyrandomness.com/Errata2020FirstEdition.pdf)

More Links:
* Incerto **Reading Club**: [Website](http://www.techincertoreadingclub.com/)
* [`StatisticalConsequencesOfFatTails`](https://github.com/MarcosCarreira/StatisticalConsequencesOfFatTails): Code and Links collected by [Marcos Carreira](https://github.com/MarcosCarreira)
* Anthony Voto: Diagnosing the SP500 [Twitter thread](https://twitter.com/votoaj/status/1427587274670329857?s=20), [GitHub Code](https://github.com/votoaj/Statistical_Consequences_of_Fat_Tails)

# Other Notes
### Contact ✉
How to reach me:
* `@MFergal` on [Twitter](https://twitter.com/MFergal)

### Contributors
Special thanks to:
* Daniel Reti: [github.com/drettt](https://github.com/drettt)

### Python Package
I started this project as a Python Package. Since then I shifted focus to python notebooks instead. Below are some notes about the packaged code and functions.

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
Roughwork:
* [How much data do I need?](https://github.com/FergM/fattails/blob/main/docs/Notes-02%20-%20Derivation%20-%20How%20much%20data%20do%20I%20need.pdf)
