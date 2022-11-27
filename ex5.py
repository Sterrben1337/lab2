n = input()
s = 0
pow = len(n) - 1
for i in n:
    s += 2 ** pow * i
    pow -= 1
print(s)