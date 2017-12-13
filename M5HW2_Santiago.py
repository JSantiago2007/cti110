# CTI 110
# M5HW2: Running Total
# Juan Santiago
# 10/19/2017

#Write a program that asks the user to enter a series of numbers.
#It should loop, adding these numbers to a running total,
#until the user enters a negative number. When a negative number is entered,
#the program should exit the loop. (It should not add the negative number to the total.) The program should then print the total before exiting. 
#Here is an example program run.
#(The user’s entries, after the “?”, are listed in bold.)
#Enter a number? 80
#Enter a number? 100
#Enter a number? 0
#Enter a number? 90
#Enter a number? -1
#Total: 270

total = 0
for i in range(5):
    newNumber = int (input( "Enter a number? " ))
    if newNumber <=-1: break
    total += newNumber 
   
print("The total is: ",total)


