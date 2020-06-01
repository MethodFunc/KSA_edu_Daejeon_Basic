num = 5

for i in range(0, num):
    for j in range(num-1, i, -1):
        print(" ", end=' ')
    for k in range(0, 2*i+1):
        print("*", end=' ')
    print()