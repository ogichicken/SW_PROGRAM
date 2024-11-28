while True:
    a = int(input("원하는 구구단의 수"))
    for x in range(1,10):
        print(a, "x", x, "=", a*x)
    b = input("한번더? y or x")
    if (b == 'y'):
        continue
    elif (b == 'x'):
        break
