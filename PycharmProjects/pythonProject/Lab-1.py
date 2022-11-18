a = int(input())
b = int(input())
c = (a * a) + (b * b)
print(c ** 0.5)



a = int(input())
b = a // 10 % 10
print(b)



a = int(input())
print(a + 2 - (a % 2))



a = int(input())
b = int(input())
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(0)



a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))



a = int(input())
b = int(input())
c = int(input())
if a > b:
    print(a) if a > c else print(c)
    print(b) if b > c else print(c)



a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a or a + c > b:
    print('YES')
else:
    print('NO')



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
