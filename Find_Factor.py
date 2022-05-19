import math
#1. Write a program which will find factors of given number and find whether the factor is even or odd.
number = 69

print("The factors of {} are,".format(number))

for i in range(1,number+1):
    if number % i == 0:
        print(i)
        if i%2==0:
            print(i, "It is an Even Number")
        else:
            print(i, "It is an Odd Number")
