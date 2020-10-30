# Saturday, ‎March ‎14, ‎2020
# 
# 3/14 is Pi day. Let's call it 1-Pi day.
# 6/28 is Tau day. Let's call it 2-Pi day.
# But today is n-Pi day, where n is what??

# n-Pi day calculator!
from math import pi

print("Month? (1, 2, ...)")
month = int(input())

print("Day? (1, 2, ...)")
day = int(input())

def days():
	s = sum % 12
	month = int(s)
	day = int((s - month) * 100)
	return [month, day]
#

request = [month % 12, day]
n = 1
sum = pi

while days() != request:
	sum += pi
	n += 1
#

print('{}/{} is {}-Pi day!'.format(month, day, n))
print('{}*pi={}\nmodulus by 12: {}'.format(n, sum, sum % 12))