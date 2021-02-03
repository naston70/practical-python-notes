# Error Checking

Although exceptions were introduced earlier, this section fills in some additioanl details about error checking and exception handling.

#### How programs fail

Python performs no checking or validation of function argument types or values. A function will work on any data that is compatible with the statements in the function.

```python

def add(x,y):
	return x+y

add(3,4)				#7
add('hello','world')	#HelloWorld
```
If there are errors in a function, they appear at runtime, as an exception.
To verify code there is a strong emphasis on testing

## Exceptions

Exceptions are used to signl errors. To raise an exception yourself, use 'raise' statement.

```python
if name not in authorized:
	raise RuntimeError(f'{name} not authorized')
```
To catch an exception use try-except

```python
try:
	authenticate(username)
except RuntimeError as e:
	print(e)
```
## Exception Handling
Exceptions propogate to first matching except

```python
def grok()
	...
	raise RuntimeError('Whoa') 

def spam():
	grok()		# Call that will raise exception

def bar():
	try:
		spam()
	except RuntimeError as e: 	#Exception caught here
	    ...

def foo():
	try:
		bar()
	except RuntimeError as e: 	# Exception does NOT arrive here
```

To handle the exception, put statements in the except block. You can add any statements you want to handle the error.

```python
def grok():
	raise RuntimeError('Whoa!')

def bar():
	try:
		grok()
	except RuntimeError as e:
		statement
		statement
```
After handling, execution resumes with the first statement after the try-except.

### Built-in Exceptions

There are about two-dozen built-in exceptions. Usually the name of the exception is indicative of what's wrong (e.g., a ValueError is raised because you supplied a bad value).

### Exception Values

Exceptions have an associated value. It contains more specific information about whats wrong





























