# this script calculates the average height of students
#in a array of student heights

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0
for height in student_heights:
  sum += height
  count += 1
average = round(sum / count)
print(average)
