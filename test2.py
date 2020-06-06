# https://hsp1116.tistory.com/33
#
# a = [7, 5, 6, 1, 3, 2, 4, 8, 9, 0]
#
# # 선택정렬
# def selection_sort(a):
#     for i in range(0, len(a)-1):
#         for j in range(i+1,len(a)):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     return a
# # 삽입정렬
# def insertionSort(a):
#     for i in range(1, len(a)):
#         key = a[i]
#         j = i - 1
#         while j>=0 and key < a[j]:
#             a[j], a[j+1] = a[j+1], a[j]
#             j -= 1
#         a[j+1] = key
#
#     return a
# # 버블 정렬
# def bubble_sort(a):
#     for i in range(0, len(a)-1):
#         for j in range(1, len(a)-i):
#             if a[j-1] > a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#     return a
#
# print(bubble_sort(a))
#
#
# a = [-7, 4, -3, 6, 3, -8, 3, 4]

# def inefficientMaxSum(a):
#     Min = min(a)
#     size = len(a)
#
#     ret = Min
#     for i in range(size):
#         for j in range(size):
#             sum = 0
#             for k in range(i, j+1):
#                 sum += a[k]
#             ret = max(ret, sum)
#     return ret

# def betterMaxSum(a):
#     n = len(a)
#     ret = min(a)
#     for i in range(0, n):
#         sum = 0
#         for j in range(i, n):
#             sum+= a[j]
#             ret = max(ret, sum)
#     return ret


# def fastestMaxSum(a):
#     n = len(a)
#     ret = min(a)
#     psum = 0
#     for i in range(n):
#         psum = max(psum, 0) + a[i]
#         ret = max(psum, ret)
#     return ret
#
# print(fastestMaxSum(a))

import random as rd


# 가장 많은 수  찾기
def majority1(a):
    size = len(a)
    majority = -1
    m_count = 0
    for i in range(size):
        v = a[i]
        count = 0
        for j in range(size):
            if a[j] == v:
                count += 1

        if count > m_count:
            m_count = count
            majority = v;
    return majority


# index 찾기
def firstIndex(a, element):
    for i in range(len(a)):
        if a[i] == element:
            return i
    return -1


def selectionSort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def insertionSort(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1


# list = [rd.randrange(1, 50) for _ in range(50)]
# list2 = [rd.randrange(1, 50) for _ in range(50)]
#
# # print(firstIndex(list, 100))
#
# selectionSort(list)
# print(list)
# insertionSort(list2)
# print(list2)

# print(list)
# print(majority1(list))

# 타겟 숫자 위치 찾기
def binsearch(a, target):
    size = len(a)
    lo = -1
    hi = size

    while lo+1 < hi:
        mid = int((lo+hi)/2)
        if a[mid] < target:
            lo = mid
        else:
            hi = mid

    return hi;

# def insecSort(a):
#     for i in range(len(a)):
#         j = i
#         while j > 0 and a[j-1] > a[j] :
#             a[j-1], a[j] = a[j], a[j-1]
#             j -= 1

list3 = [i for i in range(1, 50)]
# list4 = [rd.randrange(1, 50) for _ in range(50)]

c = binsearch(list3, 20)
# insecSort(list4)
print(c)
# print(list4)

def printDeciaml(a, b):
    iter = 0
    while a > 0:
        x = iter + 1
        if x  == 1:
            print('.', end= ' ')

        print(a / b)
        a = (a % b) * 10

printDeciaml(1, 11)