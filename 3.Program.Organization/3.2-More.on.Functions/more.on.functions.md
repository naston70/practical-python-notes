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

