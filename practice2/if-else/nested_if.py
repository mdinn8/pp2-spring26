#example-1
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#example-2
age = 17
has_license = False

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
    print("You are too young to drive")

#example-3
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
        print("Pass with good standing")
    else:
        print("Pass but missing assignment")
  else:
        print("Pass but low attendance")
else:
    print("Fail")

#example-4
att1 = 19.5
att2 = 30
final = 36

if att1+att2 >=30:
    print("Next Final")
    if att1+att2+final >= 69.5:
        print("Stipendiaaa!!!")
    elif 50 <= att1+att2+final < 69.5:
        print("Minus stipendia(")
    else:
        print("Retake")
else:
    print("Retake")

#example-5
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#example-6
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")