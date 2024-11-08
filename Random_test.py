#randomnumber
import random
attempt = 0
a= 1
b=2
# array1 = []
# array2 = []


randoms= (random.randint(1,b))

n= int(input("N:"))
    
while randoms != n:
   print("wrong")
   attempt +=1
   
   
   if n > randoms:
         print("it's too high")
         
         n= int(input("N:"))
   
   elif n < randoms:
        print("too low")
        n= int(input("N:"))
     
   if attempt == 4: # get five attempts
      print("you failed after 5 attempts the number was", randoms)
      break

if n == randoms:
       print("you guessed it after",attempt," attempts and the number was ", randoms)
   
