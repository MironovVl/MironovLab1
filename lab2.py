import math

x = int(input())
if x < 131:
	f = 77 * x ** 5 - abs(x) + 10
elif x < 141:
	f = (math.tan(x) - 75 * x + 67) ** 3 - math.tan(x)
else:
	f = 66 * x ** 5 + 2 * x ** 8
print("{:.2e}".format(f))
