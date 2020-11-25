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


def make_report(portfolio, prices):

	rows = []
	for stock in portfolio:
		current_price = prices[stock['name']]
		change = current_price - stock['price']
		summary = (stock['name'], stock['shares'], current_price, change)
		rows.append(summary)
	#print(rows)
	return rows

portfolio = read_portfolio('../../Work/Data/portfolio.csv')
prices    = read_prices('../../Work/Data/prices.csv')

report = make_report(portfolio,prices)

# Output the report
def print_report(report):
	headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_file, price_file):
	portfolio = read_portfolio(portfolio_file)
	prices    = read_prices(price_file)

	report    = make_report(portfolio, prices)
	print_report(report)
# #1 calculation of total cost of portfolio
# total_cost = 0.0
# for s in portfolio:
# 	total_cost += s['shares']*s['price']

# # Current value of portfolio
# total_value = 0.0
# for s in portfolio:
# 	total_value += s['shares']*prices[s['name']]

# print('current: ', total_value)
# print('Gain: ', total_value - total_cost)

# make_report(portfolio, prices)