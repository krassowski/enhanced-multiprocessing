# Enhanced multiprocessing

A wrapper around Python's multiprocessing, providing support for tqdm progress bars and shared arguments.

Provides simple, familiar interface with addiitonal superpowers.

### Installation

```bash
pip install enhanced_multiprocessing
```

### Example usage

```python
from enhanced_multiprocessing import Pool

def add_n(x, n):
    return x + n

# the number of processes will be set to number of cores - 1 by default
p = Pool()

# will apply add_n to the element list of length three with n=5, showing a nice progress bar along
result = p.imap(add_n, [1, 2, 3], shared_args=(5, ))

assert list(result) == [6, 7, 8]
```


### History
Originally published at [kn-bibs/pathways-analysis](https://github.com/kn-bibs/pathways-analysis/), then further developed for [krassowski/drug-disease-profile-matching](https://github.com/krassowski/drug-disease-profile-matching).
