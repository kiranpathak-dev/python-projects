# Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder

number = int(input("Which number do you want to check? "))
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")