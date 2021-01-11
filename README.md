# Fat Tails
Working through Nassim Taleb's Technical Incerto book about fat tailed statistics. [Link to ebook pdf](https://researchers.one/articles/statistical-consequences-of-fat-tails-real-world-preasymptotics-epistemology-and-applications/5f52699d36a3e45f17ae7e36)

I plan to develop the `fattails` module into a toolkit.

## Content

### Notebooks
You can find a list of notebooks in [docs/notebooks.md](./docs/notebooks.md).

Here are my favourite notebooks so far:
* [Central Limit Theorem: How the sum of Uniform values is Gaussian](./notebooks/NB-22%20-%20Visual%20Central%20Limit%20Theorem.ipynb)
* [S&P500: How geometric average return is impossible](./notebooks/Notebook-11%20-%20Ergodicity%20and%20S%26P500.ipynb)

### Functions
Right now there's just `mad()` a function to calculate mean absolute deviation.

Example:
```
$ pip install fattails
$ python

>>> import fattails
>>> from fattails.metrics import mad
>>> mad([1,2,3]) # Calculate Mean Absolute Deviation of [1,2,3]
0.6666666666666666
```

# External Resources
E-Book PDFs
* [Vol 1 of the Technical Incerto](https://researchers.one/articles/20.01.00018)
    * [Errata](https://www.fooledbyrandomness.com/Errata2020FirstEdition.pdf)

Code Repositories:
* [`ggtails`](https://github.com/David-Salazar/ggtails) for plots using R
* [StatisticalConsequencesOfFatTails](https://github.com/MarcosCarreira/StatisticalConsequencesOfFatTails) collaborative Python code and commentaries.
