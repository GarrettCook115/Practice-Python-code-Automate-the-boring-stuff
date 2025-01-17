# --ON While Loops--PG 102
# spam =0 
# if spam < 5:
#     print("Hello")
#     spam = spam +1


# Code with While loop-- repeats until it reaches 5 
# spam =0
# while spam <5:
#     print("Spam is at ",spam)
#     spam = spam +1

# example--repeates the loop until it returns false 
name = ''
while name != 'yourname':
    print("enter your name")
    name = input()
print("Thank you")


# # can use break to exit an infinit loop
while True:  #this line creates an infinite loop
    print("Who are you?")
    name =input()
    if name == 'jim':
        break       #here we have a break that can stop the loop. on pg. 110 Continue Statements
print("Thank you")