# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#bmi = weight/height*height
# Remember PEMDAS (Paranthesis, exponent, multiplication, division, adition, subtraction)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = float(weight)
bmi = new_weight/new_height**2
print(int(bmi))