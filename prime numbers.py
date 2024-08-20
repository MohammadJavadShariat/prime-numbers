#Getting a number from the user
number = int(input("give a num:"))

#Checking whether the entered number is prime
if number <= 1:
        prime = False
elif number == 2:
        prime = True
elif number >= 3:
        for i in range(2,number):
            if number % i ==0 :
                prime = False
                break
            else:
                prime = True
#Print yes or no
print(prime)