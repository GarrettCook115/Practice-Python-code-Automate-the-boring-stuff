# --checks for any number in designated range for divisability--
for i in range(1,10):
        if i %2==0:
            print(i, "Divisible by 2")
        if i %3==0:
            print(i,"Divisible by 3")
        if i%2 !=0 and i %3 !=0:
            print(i)