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

### Exercise from interpretor

>>> symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
>>> symlist = symbols.split(',')
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>> sym
symbols  symlist
>>> symlist[0]
'HPQ'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>> symlist[2] = AIG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'AIG' is not defined
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>> #cretae an empty list and append an item to it
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
>>> #you can reassign a portion of a list to another list.
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>> #Looping over list items
>>>
>>> for s in symlist: print('s =' s)
  File "<stdin>", line 1
    for s in symlist: print('s =' s)
                                  ^
SyntaxError: invalid syntax
>>> for s in symlist: print('s =', s)
...
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
>>> # Membership Tests
>>> 'AIG' in syml
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'syml' is not defined
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' not in symlist
True
>>> # Appending, inserting and deleting items
>>>
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>> #Use the insert() method to insert the symbol 'AA' as the second item in the list.
>>>
>>> symlist.insert('AA',1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> symlist.insert(1, 'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>> symlist.remove('MSFT')
>>> symlist.append('YHOO')
>>> symlist.index('YHOO')
4
>>> symlist.count('YHOO')
2
>>> symlist.remove('YHOO')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>> # SORTING
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> # Lists of anything
>>>
>>> nums =[101,102,103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
>>> #Access items in nested lists using multiple indexing operations
>>>
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][1]
'H'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>> # As a general rule better to keep nested lists simple Mixing of data and over complicated nesting... not good



