#program to calculate prime number

num=int(input("Enter the number here: "))
if num==1:
    print("Number is not prime")

elif num>1:
        for i in (2,num):
            if (num % i)== 0:
                print("Number is not prime")

            else: 
                print("Number is prime")
            break
else:
    ("Number is not prime")