# Functions

As programs start to get larger, they need to be organized

## Custom Functions

Use functions for code that is to be reused.

```python
def sumcount(n):
	```
	Returns the sum of the first n integers
	```
	total = 0
	while n > 0:
		total += n
		n -= 1
	return total
```

Then to call that function:
```python
a = sumcount(100)
```

A function is a series of statements that perform some task and return a result. The ```return```keyword is needed to explicitly specify the return value of the function.

## Library Functions

Python comes with a large standard library, modules are accesses using ```ìmport```

```python
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org')
data = u.read()

```
## Errors and exceptions

Functions report errors as exceptions. An exception causes a function to abort and may cause your entire program to stop if unhandled

Exceptions can be caught and handled. To catch, use the ```try - except ```statement.

```python
for line in f:
	fields = line.split()
	try:
		shares = int(fields[1])
	except ValueError:
		print('couldnt parse', line)

```

The name 'ValueError' must match the kind of error you are trying to catch.

It can be difficult to predict all errors, exception handling often gets added after a program has unexpectadly crashed.

## Raising Exceptions

