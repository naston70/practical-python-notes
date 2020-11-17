# SEQUENCES

###Sequence Datatypes

Python has three sequence datatypes:

- String: 'Hello', a sequence of characters
- List: [1,2,3,4]
- Tuple: (5,6,7,8)

All sequences are ordered, indexed by integers and have a length

```python

a = 'hello'
b = [1,4,5]
c = ('good', 100, 490.1)

# They all have indexed order

a[0] # -------> h
b[-1]# -------> 5
c[1] # -------> 100

# All have a length

len(a) #5
len(b) #3
```

Sequences can be replicated: ```s * n```

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequences of the same type can be concatenated ```a + b```


## SLICING

Slicing takes a subsequence from a sequence. The syntax is ```s[start:end]```. Where start and end are indexes of the subsequence you want.

```python

a = [0,1,2,3,4,5,6,7,8]

a[2:5] = [2-4]
a[-5]  = [4-8]
a[:3]  = [0-2]
```

Indices (start and end) must be integers
Slices do not include the end value.
If indices are omitted, the default to the beginning or end of the list

## SLICE RE-ASSIGNMENT

On lists, slices can be reassigned and deleted

```python
a = [0,1,2,3,4,5,6,7,8]

del a[2:4]   # [0,1,4,5,6,7,8]
```

## SEQUENCE REDUCTIONS

There are some common functions to reduce a sequence to a single value.

```python
>>> S = [1,2,3,4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['hello', 'world']
>>> max(t)
'world'
>>>
```

## ITERATION OVER A SEQUENCE

The for-loop iterates over the elements in a sequence

```python
>>> s = [1,4,9,16]
>>> for i in s:
		print(i)

1
4
9
16
>>>
```

On each iteration of the loop, you get a new item to work with. This new value is placed into the iteration variable. 

```python 

for x in s: do something

```

On each iteration, the previous value of the iteration is overwritten. After the loop finishes, the variable retains the last value.

## BREAK STATEMENT

You can use the ```break``` statement to break out of a loop early

```python
for name in namelist:
	if name == 'BOB':
		break

	...statements
```

When the ```break```statement executes, it exits the loop and moves on the next statements. The ```break``` statement only applies to the inner most loop. If this loop is within another loop, it will not break the outer loop.


## CONTINUE STATEMENT

To skip one element and move to the next one use the ```continue statement```.

```python
for line in lines:
	if line == '\n':
		continue
```

This is useful when the current item is not of interest or needs to be ignored in the processing.

## LOOPING OVER INTEGERS

If you need to count, use ```range()```

```python
for i in range:
	do_something

```
Correct syntax is ```range([start,] end [,step])```

```python

for i in range(100): #i = 0-99
	pass

for x in range(10,20): #i = 10-19
	pass

for x in range(10,50,2): # i = 10,12...,48)
	pass

```

The ending value is never included mirroring the behaviour of slices
```start```is optional with a default of 0
```step```is optional, default of 0
```range()```computes values as needed. It does not actually store a large range of numbers.

## enumerate() FUNCTION

The enumerate function adds an extra counter value to iteration 
```python

names = ['bo', 'bob', 'bobo']
for i, name in enumerate(names):
	# i = 0, name = 'bo'
	# i = 1, name = 'bob'
	# i = 2, name = 'bobo'
```

The general form is ``` enumerate(sequence [, start=0])```. Start is optional. A good example of using enumerate() is tracking line numbers while readig a file:

```python
with open(filename) as f:
	for line_no, line in enumerate(f, start=1):
		do_something
```

In the end, enumerate is a nice shortcut for:
```python

i=0
for x in s:
	do_something
	i+=1
```
Enumerate is less typing and runs slighlty faster

## FOR AND TUPLES

You can iterate with multiple iteration variables

```python 
points = [(1,4),(10,20),(23,14)]

for x, y in points:
	# x =1 y = 4
	# x =10 y = 20
	# x =23 y = 14
```

When using multiple variables, each tuple in unpacked into a set of iteration variables. The numebr of variables must match the of items in each tuple


## zip() FUNCTION

The ```zip()```function takes multiple sequences and makes an iterator that combines them.

```python

columns = ['name', 'shares', 'price']
values  = ['goog', 100, 490.1]

pairs = zip(columns, values)
# ('name', 'goog'), ('shares', 100)
```

To get the result you must iterate. You can use multiple variables to unpack tuples as shown earlier. ``` for column, value in pairs: ```

A common use of ``` zip ```is to create key/value pairs for cnstructing dictionaires.

```python
d = dict(zip(colums, values))
```

# EXERCISES.

exercise in interpreter:

```python

Type "help", "copyright", "credits" or "license" for more information.
>>> for n in range(10):
...     print(n, end = '*')
...
0*1*2*3*4*5*6*7*8*9*>>>
>>>
>>> for n in range(10,0,-1):
...     print(n, end = '*')
...
10*9
>>>
>>>
>>> for n in range(0,10,2):
...     print(n, end = '*')
...
0*2*4*6*8*>>>
>>>
>>> data = [4,9,1,25,16,100,49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
>>> for x in data:
...     print(x)
...
4
9
1
25
16
100
49
>>> for n,x in enumerate( data):
...     print(x)
...
4
9
1
25
16
100
49
>>> for n,x in enumerate( data):
...     print(n,x)
...
0 4
1 9
2 1
3 25
4 16
5 100
6 49
>>> prices = {
...         'GOOG' : 490.1,
...         'AA' : 23.45,
...         'IBM' : 91.1,
...         'MSFT' : 34.23
...     }
>>>
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>> pricelist = list(zip(prices.values(), prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
>>> a = [1,2,3,4]
>>> b = ['x','y','z','w']
>>> c = [0.2,0.4,0.6,0.8]
>>> list(zip(a,b,c))
[(1, 'x', 0.2), (2, 'y', 0.4), (3, 'z', 0.6), (4, 'w', 0.8)]
>>>

```



