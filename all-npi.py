# ‎Sunday, ‎March ‎15, ‎2020
# 
# Find the n-th pi day for every day of the year,
# including some days of the year which don't even
# exist, like February 31st!


from math import pi

# Take a number like 7.28 and convert it into [7, 28].
# Use modulus to get a reasonable month value.
def days(sum):
	s = sum % 12
	month = int(s)
	day = int((s - month) * 100)
	return [month, day]
#

months = [[], [], [], [], [], [], [], [], [], [], [], []]


for m in range(12):
	for d in range(1, 32):
		request = [m, d]
		n = 1
		sum = pi

		while days(sum) != request:
			sum += pi
			n += 1
		#
		months[m].append(n)
	#
#

print(months)