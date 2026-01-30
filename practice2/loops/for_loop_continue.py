#example-1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#example-2
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#example-3
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#example-4
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)

#example-5
a = [4, -2, 7, -5, 9]
for x in a:
    if x < 0:
        continue
    print(x)

#example-6
a = [1, 0, 3, 0, 5]
for x in a:
    if x == 0:
        continue
    print(x)
