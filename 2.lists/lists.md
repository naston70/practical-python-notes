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
Items can be changed ```c[0] = 5```

```len(c)```gives length of the list and membership is tested using ``` in or not in ```

## List Iteration and Search

use the ```for```keyword to iterate over the contents of a list

```python
for contents in the_list:
	# do something, with contents

```

To find the index of an item in the list use, ```index()``` 

```python
c.index(2)   #1
```

If the element is contained more than once, the first occurence will be returned, if the element is not found a ```ValueError```

## List removal

Items can be removed either by element value of index, once an item is removed the other items move down to fill the space. If there is more than one occurence then ```remove()```will only remove the first

```python
# using the value

c.remove(3)

# using the index

del c[0]
```

## List Sorting

Lists can be sorted in place, sorted in reverse and works with any ordered data.

```python
>>> s = [1,2,5,3,2,1,87,54,32,78]
>>> s.sort()
>>> s
[1, 1, 2, 2, 3, 5, 32, 54, 78, 87]
>>> s.sort(reverse=True)
>>> s
[87, 78, 54, 32, 5, 3, 2, 2, 1, 1]
>>>
```



