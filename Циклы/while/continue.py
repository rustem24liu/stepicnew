i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a == 0 and b == 0:
        break
    elif a ==0 or b == 0:
        continue # переходим к следущей итерации
    print(a*b)
    i+=1