# Write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100.

# 1st method
total = 0
for number in range(2,101):
    if number % 2 == 0:
        total += number
print(f"Sum of even number: {total}")

# 2nd method
# for number in range(2,101,2):
#     total += number
# print(f"Sum of even number: {total}")