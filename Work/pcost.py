# pcost.py
# Opens portfolio.csv, reads all lines and calculates total to purchase all of the shares
# Exercise 1.27


f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
total = 0
for line in f:
	row = line.split(',')
	total += int(row[1]) * float(row[2].strip('\n'))
f.close()

print(f'Total cost of portfolio: {total}')


# Expected output:
# ➜  Work git:(main) ✗ python3 pcost.py
#    Total cost of portfolio: 44671.15