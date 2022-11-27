inp = input().split()
a, n = (int(i) for i in inp)

def power(a, n):
    if n == 0:
        return "1"
    else:
        return a * n

