# Enhanced multiprocessing

A wrapper around Python's multiprocessing, providing support for tqdm progress bars and shared arguments.

Provides familiar interface with addiitonal powers.

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

# will apply add_n to the element list of length three with n=5:
result = p.imap(add_n, [1, 2, 3], shared_args=(5, ))

assert result == [6, 7, 8]
```


### History
Originally published at https://github.com/kn-bibs/pathways-analysis/, then further developed for https://github.com/krassowski/drug-disease-profile-matching.
