# http://www.prologin.org/training/challenge/demi2014/balloons
from sys import stdin

data = [int(x) for x in stdin.readline().split()]
nbBalloons = data[0]
nbCustomers = data[1]

# Get data for balloons
balloons = []
for i in range(nbBalloons):
	balloons.append([int(x) for x in stdin.readline().split()])

# Get data from customers
customers = []
for i in range(nbCustomers):
	customers.append([int(x) for x in stdin.readline().split()])

money = 0
for customer in customers:
	for balloon in balloons:
		# If the balloon meets the customer's need
		if customer[0] <= balloon[0] and balloon[0] <= customer[1]:
			# Buy it
			money += balloon[1]
			# Remove it from the pool
			balloons.remove(balloon)

print money