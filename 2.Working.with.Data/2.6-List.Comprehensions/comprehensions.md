#LIST COMPREHENSIONS


### Creating New Lists

A list comprehension creates a new list by applying an operation to each element of a sequence.

```python
>>> a = [1,2,3,4,5]
>>> b = [2*x for x in a]
>>> b[2,4,6,8,10]


>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood','jake']
>>>

```
The general syntax is [<expression> for <variable_name> in <sequence>]

##Filtering

You can also filter during the list comprehension.

```python

>>> a = [1,-5,4,2,-2,10]

>>> b = [2*x for x in a if a > 0]

>>> b = [2, 8, 4, 20]

```
##Use cases

List comps can be hugely useful, For example, you can collect values of a specific dictionary:

```python
stocknames = [s['name'] for s in stocks]
```

You can also perform dtabase-like queries on sequences.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50]
```
You can also combine a list comprehension with a sequence reduction:

```python
cost = sum([s['shares'] *s['price'] for s in stocks])
```

##General Syntax
[<expression> for <variable_name> in <sequence> if <condition>] 

Translates to:

```python
result = []
for variable_name in sequence:
	if condition:
		result.append(expression)
```
##Exercises
➜  Work git:(main) python3 -i report.py
```python
current:  28686.1
Gain:  -15985.050000000003
[('AA', 100, 9.22, -22.980000000000004), ('IBM', 50, 106.28, 15.180000000000007), ('CAT', 150, 35.46, -47.98), ('MSFT', 200, 20.89, -30.339999999999996), ('GE', 95, 13.48, -26.889999999999997), ('MSFT', 50, 20.89, -44.209999999999994), ('IBM', 100, 106.28, 35.84)]
>>> nums = [1,2,3,4]
>>> squares = [x * x for x in nums]
>>> squares
[1, 4, 9, 16]
>>> twice = [2*x for x in nums if x > 2]
>>> twice
[6, 8]
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>> # ^^ compute total cost of portfolio using a single Python statement ^^
>>>
>>> ## After you have done that, show how you can compute the current value of the portfolio using a single statement
>>>
>>> value = sum( [ s['shares'] * prices[s['name']] for s in portfolio ] )
>>> value
28686.1
>>> ### Both of the above operations are an example of a map-reduction. The list comp is mapping an operation across the list
>>>
>>>  [ s['shares'] * s['price'] for s in portfolio ]
  File "<stdin>", line 1
    [ s['shares'] * s['price'] for s in portfolio ]
    ^
IndentationError: unexpected indent
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
```

###Exercise 2.21: Data Queries

First a list of portfolio holding with more than 100 shares

```python
>>> more100 = [s for s in portfolio if s['shares'] > 100]
>>> more100
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
>>>
```

All portfolio holdings for MSFT and IBM stocks.

```python
>>> msftIBM = [s for s in portfolio if s['name'] in {'MSFT','IBM'}]
>>> msftIBM
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>>
```
A list of all portfolio holdings that cost more than $10000

```python
>>> cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>>
>>> cost10k
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
>>>
```



