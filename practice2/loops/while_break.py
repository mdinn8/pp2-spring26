#example-1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#example-2
while True:
    x = int(input())
    if x < 0:
        break
    print(x)

#example-3
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

#example-4
while True:
    x = int(input())
    if x < 0:
        break
    print(x)

#example-5
a = [1, 5, 8, 3, 9]
i = 0
while i < len(a):
    if a[i] == 3:
        break
    print(a[i])
    i += 1

#example-6
i = 1
while i <= 10:
    print(i)
    if i == 7:
        break
    i += 1

#example-7
while True:
    x = int(input())
    if x == 0:
        break
    print("You entered:", x)