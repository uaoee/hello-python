for n in range(10):
    print(n)
    pass
print("done")

for n in range(10):
    print("the square of", n, "is",n*n)
    pass
print("done")

print(2**3)


d = { 0:0, 1:1, 2:2, 3:3, 5:5 }
for i in range(6):
    try:
        print(d[i])
    except KeyError:
        pass