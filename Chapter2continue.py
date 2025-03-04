name =input("What is your username?")
while name != "jim":
    print(name)
    input("What is your username?")
    if name == "jim":
        print(name)
passw = input("What is your password?")
while passw !="pass":
    print(passw)
    input("Enter your password:")
    if passw == "pass":
        break
print("Login succesful.")