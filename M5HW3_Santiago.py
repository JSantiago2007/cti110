# CTI 110
# M5HW3: Factorial
# Juan Santiago
# 10/19/2017

#The notation n! (“n-factorial”) represents the factorial of the
#non-negative integer n. The factorial of n is the product of
#all nonnegative integers from 1 to n.
#For example:
#4! = 1 * 2 * 3 * 4 = 24
#The factorial of zero (0!) is defined to be 1.
#Assignment

#Write a program that asks the user for a nonnegative integer
#and then uses a loop to calculate the factorial of that number.
#Display the factorial 
#Here is an example program run.
#(The user’s entries, after the “?”, are listed in bold.)
#Enter a nonnegative integer? 4
#The factorial of 4 is 24
#>>>


userInteger = int( input("Please enter a number: ") )

while userInteger < 1:
    userInteger = int( input("Please enter a positive number please: ") )

factorial = 1

for currentNumber in range( 1,userInteger + 1):
    factorial = factorial * currentNumber

print()
print("The factorial of", userInteger, "is", factorial) 
