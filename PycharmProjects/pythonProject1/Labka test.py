# 1
# a = int(input())
# b = int(input())
# c = (a * a) + (b * b)
# print (c ** 0.5)


# 2
# a = int(input())
# b = a // 10 % 10
# print (b)

# 3
# a = int(input())
# print(a + 2 - (a % 2))

# 4
# a = int(input())-1
# x = a // 2 * 15 + (a + a % 2) // 2 * 5 + (a + 1) * 45
# h = 9
# m = 0
# h = h + x // 60
# x = x % 60
# m = x
# print(h, m)

a = int(input())

a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15

print(a // 60 + 9, a % 60)



# 5
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print(0)

# 6
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a, b, c))

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b:
#    print(a) if a > c else print(c)
#   print(b) if b > c else print(c)

# 7
# a1 = int(input())
# b1 = int(input())
#
# a2 = int(input())
# b2 = int(input())
#
# if a1 == a2 or b1 == b2:
#     print('YES')
# else:
#     print('NO')


# 8
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and b + c > a or a + c > b:
#     print('YES')
# else:
#     print('NO')

# 9
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(a)
# elif a == b or b == c or a == c:
#     print (b)
# else:
#     print(c)

# 10
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b:
#    a, b = b, a
# if b > c:
#    b, c = c, b
# if a > b:
#    a, b = b, a
# print(a, b, c)

