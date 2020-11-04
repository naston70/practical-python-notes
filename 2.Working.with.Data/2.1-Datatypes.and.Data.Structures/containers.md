# Containers - lists, dictionaires and sets.

Programs often have to work with many objects.
- a portfolio of stocks
- a table of stock prices

There are three main choices to use:
- Lists. Ordered data.
- Dictionaries. Unordered data.
- Sets. Unordered collection of unique items

## Lists as a Container

Use a list when the order of data matters. Lists can hold any kind of object. ie a list of tuples:

```python
portfolio = [
	('GOOG', 100, 490.1),
	('IBM', 50, 91.3),
	('CAT', 150, 83.44)
]

portfolio[0]
portfolio[2]

```

### List Construction

Building a list from scratch

```python

records = []    # Initial empty list
# Use .append() to add more items

records.append(('GGOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
```

An example when reading records from a file.

```python
records = []  # Initial empty list

with open('Data/portfolio.csv', rt) as f:
	next(f)
	for line in f:
		row = line.split(',')
		records.append((row[0], int(row[1]), float(row[2])))
```

### Dicts as a Container

Dictionaries are useful if you want fast random lookups (by key name). For example, a dictionary of stock prices.

```python

prices = {
	'GOOG': 513.25,
	'CAT' : 87.22,
	'IBM' : 93.37,
	'MSFT': 44.12
}
```
example lookups...

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
```

## Dict Construction

```python

prices = {}

# Inset new items

prices['GOOG'] = 513.25
prices['CAT']  = 87.22
prices['IBM']  = 93.37
```

Populating a dict from the contents of a file:

```python

prices = {}

with open('Data/prices.csv', 'rt') as f:
	for line in f:
		row = line.split(',')
		prices[row[0]] = float(row[1])
```








