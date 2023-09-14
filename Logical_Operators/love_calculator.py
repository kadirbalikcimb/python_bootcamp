"""You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amount_t = name1.lower().count("t") + name2.lower().count("t")
amount_r = name1.lower().count("r") + name2.lower().count("r")
amount_u = name1.lower().count("u") + name2.lower().count("u")
amount_e = name1.lower().count("e") + name2.lower().count("e")

amount_l = name1.lower().count("l") + name2.lower().count("l")
amount_o = name1.lower().count("o") + name2.lower().count("o")
amount_v = name1.lower().count("v") + name2.lower().count("v")

love_score = amount_t*10+amount_r*10+amount_u*10+amount_e*10+amount_l+amount_o+amount_v+amount_e

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score<50 and love_score>40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

