#example-1
print(15-9)

#example-2
sum1 = 50+50
sum2 = sum1 + 150
sum3 = sum2 + sum1
print(sum3)

#example-3
x = 97
y = 13

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#example-4
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#example-5
x = 5555
y = 846

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#example-6
x = 5

print(1 < x < 10)

print(1 < x and x < 10)

#example-7
x = 97
print(not(99 < x and x > 999))

#example-8
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

#example-9
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#example-10
text = "Salem, Alem!"

print("S" in text)
print("Zh" in text)
print("z" not in text)

#example-11
x = 226
y = 512
print(x & y)
print(x | y)
print(x ^ y)

#example-12
print((877-521)+(154-220))