# pcost.py
# Opens portfolio.csv, reads all lines and calculates total to purchase all of the shares
# Exercise 1.27

def portfolio_cost(filename):
	f = open('Data/portfolio.csv', 'rt')
	headers = next(f).split(',')
	cost = 0
	for line in f:
		row = line.split(',')
		cost += int(row[1]) * float(row[2].strip('\n'))
	f.close()
	return cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ', cost)


#print(f'Total cost of portfolio: {total}')


# Expected output:
# ➜  Work git:(main) ✗ python3 pcost.py
#    Total cost of portfolio: 44671.15