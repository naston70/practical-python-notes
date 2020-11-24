#Scripting

###What is a Script?

A script is a program that runs a series of statments and stops.
If you write a useful script it will grow in features and functionality. You may want to apply it to other related problems. Over time it could become a critical application so its important to stay organized.

###Defining Things

Names must always be defined before they get used later.
The order is important. You almost always put the definitions of variables and functions near the top.

###Defining Functions

It is a good idea to put all of the code related to a single task all in one place. Use a function...

```python

def read_prices(filename):
	prices = {}
	with open(filename) as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			prices[row[0]] = float(row[1])
	return prices

```
A function also simplifies repeated operations:

```python
old_prices = read_prices('old.csv')
new_prices = read_prices('new.csv')
```