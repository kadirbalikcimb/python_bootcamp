# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
i = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print(student_heights[n])
    i+=1
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
print(i)
total_height = 0
for height in student_heights:
    total_height+=height

print(total_height)
average_height = round(total_height/i)
print(average_height)
