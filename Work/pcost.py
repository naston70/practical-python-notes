# pcost.py
# Opens portfolio.csv, reads all lines and calculates total to purchase all of the shares
# Exercise 1.27

# def portfolio_cost(filename):
# 	f = open('Data/missing.csv', 'rt')
# 	headers = next(f).split(',')
# 	cost = 0
# 	for line in f:
		
# 		row = line.split(',')
# 		try: 
# 			cost += int(row[1]) * float(row[2].strip('\n'))
# 		except ValueError:
# 			print('Field missing', line)

# 	f.close()
# 	return cost

# cost = portfolio_cost('Data/missing.csv')
# print('Total cost: ', cost)


# #print(f'Total cost of portfolio: {total}')


# # Expected output:
# # ➜  Work git:(main) ✗ python3 pcost.py
# #    Total cost of portfolio: 44671.15
import csv, sys

def portfolio_cost(filename):
	cost = 0
	f = open(filename)
	#print('here', f.read())
	rows = csv.reader(f)
	headers = next(rows)
	for row in rows:
		shares = row[1]; price = row[2]
		try:
			cost += int(shares) * float(price)
		except ValueError:
			print('Field missing', row)
	f.close()
	return cost


if len(sys.argv) == 2:
	filename = sys.argv[1]
	print(filename)
    
else:
    filename = 'Data/portfolio.csv'
    print('hard-coded')

cost = portfolio_cost(filename)
print('Total cost: ', cost)