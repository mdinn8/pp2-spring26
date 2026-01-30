#example-1
a = 33
b = 200

if b > a:
    pass

# having an empty if statement like this, would raise an error without the pass statement

#example-2
age = 16

if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")

#example-3
score = 85

if score > 90:
    pass # This is excellent
print("Score processed")

#example-4
value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass #zero case
else:
    print("Positive value")

#example-5
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet