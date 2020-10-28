# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payments = 12
extra_payment_value = 1000.0
months = 0

while principal > 0:
	while extra_payments > 0:
		
		principal = principal * (1+rate/12) - payment - extra_payment_value
		total_paid = total_paid + payment + extra_payment_value
		extra_payments -= 1
		months +=1

	principal = principal * (1+rate/12) - payment
	total_paid = total_paid + payment
	months +=1
print('total months:', months)

print('total_paid:', total_paid)