# suma de los números pares de 10 a 5000 menos el 100 y el 1000

input("suma de los numeros pares entre 10 y 5000")

n = 5000
h = 0
while n >= 10:
    if n%2 == 0:
        print (n)
        h += n
    n -= 1

h -= 1100
print ('la su suma es: %i' % h)
