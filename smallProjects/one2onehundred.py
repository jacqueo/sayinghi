# for loop from 1 to 100, printing every number divisible by 5 and 18.

for number in range(1, 100):
	if number % 5 == 0 or number % 18 == 0:
		print(number)