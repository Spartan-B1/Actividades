




limite = 4
n = 0
e = 0

def fact(n):
    i = 1
    num = 1
    while i <= n:
        num *= i
        i += 1
    return num

while n < limite:
	e += 1/fact(n)
	n = n + 1


print("Factorial: ",fact(1))
print("Exponencial: ",e)
