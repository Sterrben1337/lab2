inp = input().split()
x, y, z = (int(i) for i in inp)

def Election(x, y, z):
    if x + y + z >= 2:
        return 1
    elif x + y + z < 2:
        return 0
print(Election(x,y,z))