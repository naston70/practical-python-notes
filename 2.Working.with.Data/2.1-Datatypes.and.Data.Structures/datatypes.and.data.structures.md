Tuples and dictionaries.

## Primitive Datatypes

Python has a few primitive types of data: integers, floating point numbers and strings

## None Type

```email_address = None ```

```None```is often used as a placeholder for optional or missing value. It evaluates as ```False```in conditionals

```python
if email_address:
	send_email(email_address, msg)
```
## Data Structures

Real programs have more complex data. For example info abotu stocks, as per previous examples

```100 shares of 'Goog' at $490.20```

This object can be represented by three parts:

1. Name or symbol of the stock
2. Number of shares
3. Price

## Tuples


A tuple is a collection of values grouped together.

```python
s = ('Goog', 100, 490.1)

s = 'Goog', 100, 490.1
```

Sometimes the () are omitted in the syntax.

Special cases (0-tuple, 1-tuple)

```python
t = ()
w = ('Goog',)
```
Tuples are often used to represent simple records or structures. Typically it is a single object of multiple parts - a good analogy A tuple is like a single row in a database table

Tuple contents are ordered - like an array (list)
```python
s = ('GOOG', 100, 490.1)
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1
```

However contents cannot be modified. You can however make a new tuple based on a current tuple. 

```python
s = ('GOOG', 100, 490.1)
s = (s[0], 75, s[2])
>>> s
('GOOG', 75, 490.1)
```

## Tuple Packing
Tuples  are more about packing related items together into a single entity.

```s = ('Goog', 100, 490.1)```

The tuple is then easy to pass around to other parts of a program as a single object

## Tuple Unpacking 
To use the tuple elsewhere, you can unpack its parts into variables.
```name, share, price = s```

Variables on the left must match amount in the tuple structure.

## Tuples vs. Lists

Tuples look like read-only lists. However, tuples are most often used for a single item consisting of multiple parts. Lists are usually a collection of distinct items, usually all of the same type. 

```python
record = ('Goog', 100, 490,1) #tuple

symbol = ['Goog', 'IBM', 'AAPL'] #list
```

## Dictionaries

A dictionary is a mapping of keys to values. It is also sometimes called a hash table or associative array. The key serves as indicies for accessing values.

```python
s = {'name': 'GOOG',
	 'shares': 100
	 'price': 490.1
}
```

## Common Operations

Getting values from a dictionary using the key names.

```python
print(s['name'], s['shares'])
GOOG 100
```

To add or modify values assign using the key names.

```python
s['shares'] = 75
s['date'] = '6/6/2020'
```
To delete a value use the ```del```statement. ```del s['date']```

Why use dictionaries?

Dictionaries are useful when there are many different values and those values might be modified or manipulated. Dictionaries make code more readable.

Exercises.