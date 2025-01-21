#randomnumber
import random
attempt = 0
a= 1
b=2
# array1 = []
# array2 = []

#range will be "N" times depending on user input we'll display that many numbers in our array
randoms= (random.randint(1,6))

n= int(input("N:"))
    
while randoms != n:
   print("wrong")
   attempt+=1
   n= int(input("N:"))
   

   if attempt == 5:
      print("you failed after 5 attempts"+"The answer was", randoms)
      break 

   elif n == randoms:
       print("you guessed it after",attempt," attempts" , randoms, "Was the number")
       

   

  