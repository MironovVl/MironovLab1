import math

n = int(input('n = '))
m = int(input('m = '))
tmp = 0
for i in range(1, n + 1):
	tmp += 77 * i ** 5 - abs(i) + 10
f = 2 * tmp
tmp = 0
for i in range(1, n + 1):
	for j in range(1, m + 1):
		tmp += i ** 3 / 28 + math.e ** i
f += tmp * 33
print("{:.2e}".format(f))
n = input()
