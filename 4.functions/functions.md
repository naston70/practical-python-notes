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