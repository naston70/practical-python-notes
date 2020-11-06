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

