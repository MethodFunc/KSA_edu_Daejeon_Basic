# # a = []
# # n = int(input(' '))
# count_0 = 0
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_5 = 0
# count_6 = 0
# count_7 = 0
# count_8 = 0
# count_9 = 0
# #
# # a = [i for i in range(1, n+1)]
# #
# # b = a.copy()
# #
# # for i in range(len(b)):
# #     if b[i] > 10 and b[i] < 100:
# #         print(b[i] / 10)
# #
#
#
# print(count)
# # c = str(b).split('.')
# #
# # for i in range(len(c)):
# #     c[i] = int(c[i])
# # print(c)
#

# n = int(input(' '))
#
# for i in range(0, n-2):
#     for j in range(0, n-i-1):
#         print(' ', end='')
#     for k in range(0, 2*i-1):
#         print('*', end='')
#     print()
#
# for i in range(n-2, 0, -1):
#     for j in range(n-i-1, 0, -1):
#         print(' ', end='')
#     for k in range(2 * i - 1, 0, -1):
#         print('*', end='')
#
#     print()
#
#

# sum_sec = 0
# for i in range(24):
#     for j in range(61):
#         if '3' in str(i) or '3' in str(j):
#             sum_sec += 60
#
# print(sum_sec)

# n = int(input('1 ~ 1000 : '))
# list1 = []
# list2 = []
# list3 = []
# for a in range(1, n+1):
#     if a < 10:
#         b = list1.append(a)
#
#     if a >= 10 and a < 100:
#         b = list1.append(int(a / 10))
#         c = list2.append(a % 10)
#
#     if a >= 100 and a < 1000:
#         b = list1.append(int(a / 100))
#         c = a % 100
#         d = list2.append(int(c / 10))
#         e = list3.append(c % 10)
#
# # print(list3)
# count = []
# for i in range(0,10):
#         count.append(list1.count(i) + list2.count(i) + list3.count(i))
#
# print('0:{}개, 1:{}개, 2:{}개, 3:{}개, 4:{}개, 5:{}개, 6:{}개, 7:{}개, 8:{}개, 9:{}개'.format(count[0],count[1],count[2],count[3],count[4],count[5],count[6],count[7],count[8],count[9]))


# n = int(input('input : '))
#
# sum = 0
# mul = 0
# for i in range(1, n+1):
#     sum += i
#
# sum = sum ** 2
#
# for i in range(1, n+1):
#     mul += i ** 2
#
# print(sum-mul)

# def sizer(a, n):
#     if ord(a) > 64 or ord(a) < 91:
#         a = ord(a) + n
#         if a > 91:
#             a = 65 + (a - 90)
#     return chr(a)
#
# word = input('Word : ')
# n = int(input('Cicle : '))
#
# for i in range(len(word)):
#     print(sizer(word[i], n), end = '')
#
# print(sizer('A', 5))
