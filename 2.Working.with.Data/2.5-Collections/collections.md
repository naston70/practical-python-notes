#COLLECTIONS MODULE

The ```collections``` module provides a number of useful objects for data handling.

###Example: Counting Things

If you what to tabulate the total shares of each stock

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

There are two IBM and two GOOG entries in this list. The shares need to be combined together somehow.

###Counter

Solution: Use a ```Counter```

```python

from collections import Counter

total_shares = Counter()

for name, shares, price in portfolio:
	total_shares[name] += shares

total_shares['IBM']        #150

```

###Example One-Many Mappings

Problem: You want to map a key to multiple values:

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

Like above, the key ```IBM``` should have two different tuples instead

Solution: Use ```defaultdict```

```python

from collections import defaultdict

holdings = defaultdict(list)

for name, shares, price in portfolio:
	holdings[name].append((shares,price))

holdings['IBM']			# [ (50, 91.1), (100, 45.23) ]
```
The defaultdict ensures that everytime you access a key you get a default value


###Example: Keeping a History

Problem: We want a history of the last N things. Solution use a ```deque```

```python
from collections import deque

history = deque(maxlen=N)

with open(filename) as f:
	for line in f:
		history.append(line)
		...
```
#EXERCISES

The collections module might be one of the most useful library modules for dealing with special purpose kinds of data handling problems such as tabulating and indexing.


Suppose you want to tabulate the total number of shares of each stock. This is easy using ```Counter```objects.

```python

python3 -i report.py
current:  28686.1
Gain:  -15985.050000000003
[('AA', 100, 9.22, -22.980000000000004), ('IBM', 50, 106.28, 15.180000000000007), ('CAT', 150, 35.46, -47.98), ('MSFT', 200, 20.89, -30.339999999999996), ('GE', 95, 13.48, -26.889999999999997), ('MSFT', 50, 20.89, -44.209999999999994), ('IBM', 100, 106.28, 35.84)]
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> from collections import Counter
>>> holdings= Counter()
>>> for s in portfolio:
...     holdings[s['name']] += s['shares']
...
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

