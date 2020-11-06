# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
	'''	Opens a given portfolio file and reads it into a list of tuples'''
	portfolio = []

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		
		for row in rows:
			d = {
				'name' : row[0],
				'shares' : int(row[1]),
				'price' : float(row[2])
			}
			portfolio.append(d)
	
	return portfolio



def read_prices(filename):
	'''
	Read csv into dict of names and prices
	'''
	d = {}
	f = open(filename, 'rt')
	rows = csv.reader(f)
	
	for row in rows:
		try:
			d[row[0]] = float(row[1])
		except IndexError:
			pass
		
	return d

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

#1 calculation of total cost of portfolio
total_cost = 0.0
for s in portfolio:
	print(s)
	total_cost += s['shares']*s['price']

# Current value of portfolio
total_value = 0.0
for s in portfolio:
	total_value += s['shares']*prices[s['name']]

print('current: ', total_value)
print('Gain: ', total_value - total_cost)