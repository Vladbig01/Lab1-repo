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

# В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок. Выведите два целых числа: время окончания урока в часах и минутах. При решении этой задачи нельзя пользоваться циклами и условными инструкциями.
a = int(input())
num_peremen = a - 1
time_peremen = (num_peremen // 2 * 20) + (num_peremen % 2) * 5
time_urok = a * 45

time_all_minutes = time_peremen + time_urok

hours = time_all_minutes // 60
minutes = time_all_minutes % 60

print(hours + 9)

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



