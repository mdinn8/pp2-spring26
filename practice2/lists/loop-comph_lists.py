#example-1
thislist = ["apple", "banana", "orange", "mango", "papaya", "pineapple"]
for x in thislist:
    print(x)

#example-2
mylist = ["onepiece", "naruto", "hunterxhunter", "black clever"]
for i in range(len(mylist)):
    print(mylist[i])

#example-3
list = ["asus", "acer", "macbook", "lenovo", "huawei"]
i = 0
while i < len(list):
    print(list[i])
    i+=1

#example-4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#example-5
list = ["georgia armani", "round lab", "skin 1004", "chanel", "hourglass"]
newlist = []

for x in list:
    if "a" in x:
        newlist.append(x)

print(newlist)

#example-6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#example-7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#example-8
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

#example-9
newlist = [x for x in range(97)]
print(newlist)

#example-10
nllist = [x for x in range(512) if x < 8]
print(nllist)

#example-11
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['Salem' for x in fruits]

print(newlist)

#example-12
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
