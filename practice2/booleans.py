#example-1
print(10 > 9)
print(5 == 4)
print(10 < 9)

#example-2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example-3
print(bool("Hello"))
print(bool(97))

#example-4
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#example-5
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example-6
def myFunc():
    return True

print(myFunc())

#example-7
def func():
  return False

if func():
  print("YES")
else:
  print("NO")

#example-8
x = 1004
print(isinstance(x, int))