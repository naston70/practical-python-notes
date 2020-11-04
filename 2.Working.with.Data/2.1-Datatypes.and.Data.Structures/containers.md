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