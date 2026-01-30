#example-1
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

#example-2
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

#example-3
i = 0
while i < 5:
    x = int(input())
    if x < 0:
        continue
    print(x)
    i += 1

#example-4
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

#example-5
i = -2
while i <= 2:
    if i == 0:
        i += 1
        continue
    print(i)
    i += 1
