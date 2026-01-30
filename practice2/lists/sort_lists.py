#example-1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example-2
list = [97, 2008, 1004, 10, 85, 99]
list.sort()
print(list)

#example-3
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#example-4
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#example-5
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#example-6
mylist = ["clash of clans", "github", "instagram", "brawl stars", "telegram", "wsp"]
mylist.reverse()
print(mylist)