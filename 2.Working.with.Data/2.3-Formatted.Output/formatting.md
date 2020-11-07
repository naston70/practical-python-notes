# Formatting

Working with data you oftwn want to produce structured output (tables etc)

### String Formatting

One way to format strings in Python 3.6+ is with f-strings

(interpreter)

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
```

It is commonly used with print

### Format codes

Common codes include (After the : inside the {})

```
d 	Decimal integer
b 	Binary integer
x	Hex int
f 	Float
s 	String
c 	Char
```

Common modifiers adjust the field width and decimal precision:

```
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```

### Dictionary Formatting

```format_map()```method applies string formatting to a dictionary of values:

```python

>>> s = {
	'name'  : 'IBM',
	'shares': 100,
	'price' : 91.1
}

>>> '{name:>5s} {shares:5d} {price:5.2f}'.format_map(s)
```

### format() method

There is a method format() that can apply formatting to arguements or keyword arguments.

### The % formatting operator
Will require a single item or tuple on the right. 

### Exercises on interpreter