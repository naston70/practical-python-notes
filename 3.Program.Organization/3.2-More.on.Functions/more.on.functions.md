###Calling a Function

Consider this function:

```python
def read_prices(filename, debug)
```

You can call the function with positional arguments:

```python
prices = read_prices('prices.csv', True)
```
Or you can calle the function with keyword arguments

```python
prices = read_prices(filename = 'prices.csv', debug = True)
```

###Default Arguments

Sometimes you may want an argument to be optional. If so assign a default value in the function definition:

```python
def read_prices(filename, debug = False)
```
If a default value is assigned, the arument is optional in function calls

```python
d = read_prices('prices.csv')
e = read_prices('prices.csv', True)
```
Defaults must appear at the end of the arguments list (all non-optional go first)

###Prefer keyword arguments for optional arguments

Compare and contrast these two different calling styles:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```
In most cases keyword arguments improve code clarity, especially for arguments that serve as flags or which are related to optional features.

###Design Best Practice:

Always give short but meaningful names to function arguments. Someone using a function may want to use the keyword calling style.

```python
d = read_prices('prices.csv', debug=True)
```

Python development tools will show the names in help features and documentation.

###Returning Values

The ```return``` statement returns a value

```python
def square(x):
	return x*x
```
If no return value is given or return is missing, ```None``` is returned

###Multiple Return Values
