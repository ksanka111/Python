# Несколько способов нахожденияНа факториала
# Способ 1 - давольно большой

fact = int(input('1. Введите число: '))
dgt = fact
a = 0
c = 1
while fact > 0:
    a = fact
    c = c*a
    fact -=1
print('Факториал', dgt, '=',c)

# Способ 2
a = int(input('2. Введите число: '))
dgt = a
fact_2 = 1
while a > 0:
    fact_2 *= a
    a -= 1
print('Факториал', dgt, '=',fact_2)

# Способ 3
a = int(input('3. Введите число: '))
dgt = a
fact_3 = 1
for i in range(2, a+1):
    fact_3*=i
print('Факториал', dgt, '=',fact_3)

# Способ 4
def fact_4(n):
    if n != 0:
        return n * fact_4(n - 1)
    else:
        return 1
print('Факториал 5 =', fact_4(5))
#
# Способ 5, почти как и 4ый, но немного короче
def fact_5(a):
    if a == 0:
        return 1
    return a * fact_5(a-1)
print('Факториал 6 =',fact_5(6))
