print("my name is")
for i in range(5): #prints the name jim 5 times with the i count aswell.
    print('jim (' + str(i) + ')')

#rewritten as a while loop
print("my name is")
i =0 
while i < 5:
    print("Jim (" + str(i) + ')')
    i = i+1



count = 0  #we add our beginning count 0 with the current number each time 100 times. 
for num in range(100):
    count = num + count #num starts at 0 as we count up. num will equal 1 + 0 (num + count) this equals 1, then the new count will be 1 while our num moves on to 2. now our (num + count) will = 3
                        #the new coutn is now 3 while our num is now on 3 aswell in the range. 
                        # num + count = 6. 6 becomes the new count while our num is now 4. 6+4 (count +num) = 10. coutn is now 10 and our nu is at 7 etc...
    print(count)        # we print each output per iteration as we count and add them both until we hit 100 attempts.


