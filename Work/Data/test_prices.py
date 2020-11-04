prices = {} # Initial empty dict

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
        	prices[row[0]] = float(row[1])
        except IndexError:
        	print('IndexError')

    print(prices)