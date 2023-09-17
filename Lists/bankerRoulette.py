# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lengthOfList = len(names)

print(lengthOfList)

ranIndex = random.randint(1, lengthOfList) - 1

print(random.choice(names)
      )
print(f"{names[ranIndex]} is going to buy the meal today!")