#example-1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#example-2
for x in "Programming":
    print(x)

#example-3
s = "P7thh000nby6trh"
for i in s:
    if s.isalpha():
        print(s)

#example-4
for x in range(6):
    print(x)

#example-5
for x in range(2, 6):
    print(x)

#example-6
for x in range(2, 30, 3):
    print(x)

#example-7
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#example-8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#example-9
for x in [0, 1, 2]:
    pass