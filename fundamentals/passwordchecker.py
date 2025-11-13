password = input("Masukakn passwor mu: ")
x = 0
if any(char.islower() for char in password):
    x += 1

if any(char.isupper() for char in password):
    x += 1

if any(char.isdigit() for char in password):
    x += 1

if any(not char.isalnum() for char in password):
    x += 1

if len(password) >= 8:
    x += x

if x == 1:
    print("Butut")
elif x == 2:
    print("lumayan butut")
elif x == 3:
    print("lumayan alus")
elif x == 4:
    print("alus")
elif x == 5:
    print("alus pisan")
elif x == 0:
    print("Babarian jebol")

print(f"'{password}' is level {x}")
