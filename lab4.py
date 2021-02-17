import math


def f(n):
	if n == 1:
		return 10
	elif n == 0:
		return 9
	else:
		return f(n - 1) ** 2 / 81 + math.sin(f(n - 2)) - 36


n = int(input('n = '))
print("{:.2e}".format(f(n)))
