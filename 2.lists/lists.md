## Creating a List

Use square brackets to define a list literal

```python
names = ['a', 'b', 'c']
```

Lists can also be created by other methods

```python
line = '10,20,30,40'
row = line.split(',')

>>>row
['10','20','30']
```

# List Operations

Lists can hold items of any type. Add new items to a list using `.append()` Adds it to the end of the list. Use `insert(1)` to choose where the item is placed in the list.

Use + to add lists together (concatenate)

```python
a = [1,2,3]
b = [4,5,6]
c = a+b
[1,2,3,4,5,6]
```

List are indexed by integers starting at 0 and a negative indices starts the count from the end

```python
>>>c[0]
1

>>>c[-1]
6
```

