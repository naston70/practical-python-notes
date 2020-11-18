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







