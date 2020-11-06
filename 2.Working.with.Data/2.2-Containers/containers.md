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

Modify the code to handle the empty line.

```python
prices = {} # Initial empty dict

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
        	prices[row[0]] = float(row[1])
        except IndexError:
        	print('IndexError')

```

## Dictionary Lookups

Testing the existence of a key

```if key in d: do_something```

### Composite keys.

Almost any type of value can be used as a dictionary key in Python. A dictionary key must be of a type that is immutable. For example, tuples.

```python
holidays = {
	(1,1) : 'New Years',
	(3,14): 'Pi Day',
	(9,13): 'Programmers Day'
}
```

Then to access the value:

```holiday[3,14] >>>> 'Pi day'```

A list, set or another dictionary can serve as a dictionary key, because lists and dictionaries are mutable

## Sets

Sets are a collection of of unordered unique items

```python
tech_stocks = {'IBM', 'AAPL', 'MSFT'}

# or with an alternative syntax

tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Sets can be useful for membership tests.

```python 
>>>tech_stocks
set({'IBM', 'AAPL', 'MSFT'})
>>> 'IBM' in tech_stocks
True
>>>'TESLA' in tech_stocks
False
```
Sets are also useful for duplicate elimination

```python

names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```
## Exercise

A list of tuples:

Code from previous exercise should look similar to the following:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Create report.py, in that file define a function read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples. 


Sample code for first part of exercise

```python
# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
	'''	Opens a given portfolio file and reads it into a list of tuples'''
	portfolio = []

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		
		for row in rows:
			#print(row)
			holding = (row[0], int(row[1]), float(row[2]))
			portfolio.append(holding)
		
		return portfolio

```



