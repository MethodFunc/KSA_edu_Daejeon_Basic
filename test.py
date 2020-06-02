#https://hsp1116.tistory.com/33

a = [7, 5, 6, 1, 3, 2, 4, 8, 9, 0]

def selection_sort(a):
    for i in range(0, len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j>=0 and key < a[j]:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
        a[j+1] = key

    return a

def bubble_sort(a):
    for i in range(0, len(a)-1):
        for j in range(1, len(a)-i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a

print(bubble_sort(a))
# def quick_sort(a):
# print(insertionSort(a))
# print(selection_sort(a))
