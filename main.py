nachalo = int(input("начало- "))
konec = int(input("конец- "))
for num in range(max(2, nachalo), konec + 1):
    for i in range(max(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")