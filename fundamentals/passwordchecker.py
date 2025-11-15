password = input("Input your password: ")
def passwordChecker(password):
    global x
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
        x += 1

    if len(password) < 8:
        x -= x

    print(f"Password level: {x} |",end=" ")

    if x == 1:
        print("very bad")
    elif x == 2:
        print("bad")
    elif x == 3:
        print("maybe good")
    elif x == 4:
        print("good")
    elif x == 5:
        print("strong")
    elif x == 0:
        print("wtf are you doing?? your password need to be 8 digit!!")

   
passwordChecker(password)
