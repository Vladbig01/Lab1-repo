# 1 Гипотенуза
a = int(input())
b = int(input())
c = (a * a) + (b * b)
print(c ** 0.5)


# 2 Число десятков
a = int(input())
b = a // 10 % 10
print(b)


# 3 Следующее чётное
a = int(input())
print(a + 2 - (a % 2))


# 5 Какое из чисел больше
a = int(input())
b = int(input())
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(0)


# 6 Максимум из трёх
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))


# 8 Существует ли треугольник
a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a or a + c > b:
    print('YES')
else:
    print('NO')


# 9 Количество равных из трёх
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
   print(3)
elif a == b or b == c or a == c:
   print(2)
else:
   print(0)    


# 10 Упорядочить три числа
a = int(input())
b = int(input())
c = int(input())
if a > b:
   a, b = b, a
if b > c:
   b, c = c, b
if a > b:
   a, b = b, a
print(a, b, c)
