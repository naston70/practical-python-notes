import csv

def read_prices(filename):
	f = open(filename, 'rt')
	rows = csv.reader(f)
	headers = next(rows)
	d = {}
	for row in rows:
		try:
			d[row[0]] = float(row[1])
			# d = {
			# 	'name': row[0],
			# 	'price': float(row[1])
			# }
		except IndexError:
			print('missing')
		

	return d

