p = 907
q = 233
n = p * q
f = (p-1)*(q-1)
e = 696
d = 151

number = int(input('Write a number _______ '))
K_O = (n, e)
K_C = (n, d)

sign = 0
stop = 1
i=0

while stop != 0:
	if i != 0:
		number = int(input('Write a number _______ '))
		sign = input('shifr - 1, not - 0 _______ ')
		i+=1
	if sign == 0:
		print(1)
		number = number**(e*(n//2))
		print(number)
		stop = input('Would you like to continue? (yes - 1, no - 0) _______ ')
	elif sign == 1:
		number = number**(d*(n//2))
		print(number)
		stop = input('Would you like to continue? (yes - 1, no - 0) _______ ')

