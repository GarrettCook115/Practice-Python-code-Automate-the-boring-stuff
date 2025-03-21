while True:
    name = input("Who are you?")
    if name !="joe":
        continue #continue utilized to continuously iterate the while true statement aslong as name != joe. Will continue and break to the next section after appropriate input. "joe as name"

    print(" Hello" + name + "Enter your password")
    password = input()
    if password != "pass":
        print("Wrong pass")
        #if the wrong password is inserted then the entire while loop will start over from the first question asking for the name. 
    if password == "pass":
        break
print("Logon accepted")
    
