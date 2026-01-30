#example-1
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

#example-2
a = 97
b = 10
c = 208
if a > b or a > c:
    print("At least one of the conditions is True")

#example-3
x = 7778
y = 45324

if not x > y:
    print("x is NOT greater than y")

#example-4
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
  
#example-5
temperature = 26
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")
    
#example-6
username = "mdinnnnn"
password = "qwertyyy"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")

#example-7
score = 86
if score >=69.5 and score <= 100:
    print("Stipendiaaaaa")