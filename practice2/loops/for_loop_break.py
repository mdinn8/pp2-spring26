#example-1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#example-2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#example-3
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#example-4
a = [3, 6, 8, -1, 5]
for x in a:
    if x < 0:
        break
    print(x)

#example-5
for i in range(1, 11):
    print(i)
    if i == 7:
        break

#example-6
a = [5, 2, 4, 0, 9]
for x in a:
    if x == 0:
        break
    print(x)

#example-7
s = "python"
for ch in s:
    if ch == "h":
        break
    print(ch)
