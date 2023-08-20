# Write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num_of_students = 0
total_height = 0
for height in student_heights:
    num_of_students += 1
    total_height += height
print(total_height)
print(num_of_students)
average_height = round(total_height/num_of_students)
print(f"Average height = {average_height}")

# Using sum() and len()
# total_height = sum(student_heights)
# num_of_students = len(student_heights)
# average_height = round(total_height/num_of_students)
# print(average_height)