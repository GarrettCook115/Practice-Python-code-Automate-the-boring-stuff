# --Boolean
# --"==" assigns what it's equal to, 
# while "=" assigns what the variable is
# "Use and,or,not operators"
# True and False = False,True or False =True,
# if, else statements. Else statements are only followed by if statements when they are false.
n = input("input password")
nt = int(input("Number:"))

while n != "Password":
    print("acccess Denied")
    n = input("input password")

    if n == "Password":
        print("Correct")
    else: 
      print("Wrong")
        
if nt == 1:
      print("1")
else:
      print("You chose number"+str(nt))


# elif statements
name = input("Input your name")
age = int(input("Age:"))

if name =="Jim":
    print("Hello")
    
elif age <100:
      print("I don't know you.")
      
elif age > 100:
     print("Nomb")
    
elif age > 3:
    print("Yes")


