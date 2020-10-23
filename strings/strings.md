### Notes on Strings

```

'\n' -- Line feed
'\r' -- Carriage return
'\t' -- Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash
```

Each char in a string is stored internally as a Unicode 'code-point' which is an int

String indexing use an int index starting at 0

Slice string or select substrings specifying a range of indices with :

String methods - many string methods, such as 

```python
s.find(x)
s.index(x)  
```
All methods found by using help 
```python
help(str)
```

## f-Strings

A string formatted expression substittion
```python
name = 'IBM'
shares = 100
price = 91.1

a = f{names:>10s} {shares:10d} {price:10.2f}
```


Exercise for strings are through the interpreter.

Simple setup is to set variable below and follow along.

```python
symbols = 'AAPL, IBM, MSFT, YHOO, SCO'

```

### Exercises on interpreter