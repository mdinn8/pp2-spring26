#example-1
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#example-2
n = int(input())
d = {}

while n > 0:
    line = input().split()
    if line[0] == "set":
        key = line[1]
        value = line[2]
        d[key] = value
    if line[0] == "get":
        key = line[1]
        if key in d:
            print(d[key])
        else:
            print(f"KE: no key {key} found in the document")
    n -=1

#example-3
i = 1
while i < 6:
    print(i)
    i += 1

#example-4
i = 97
while i > 0:
    if i % 2 == 0:
        print(i)
    i -= 1

#example-5
n = 2878
sum = 0
while n > 0:
    sum += n%10
    n /= 10
print(sum)