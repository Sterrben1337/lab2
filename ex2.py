x = int(input())

for i in range(2, 30001):
    if not x % i:
        print(i)
        break