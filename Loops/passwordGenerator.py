#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""pw = ""
for l in range(1, nr_letters+1):
    pw+=random.choice(letters)

for s in range(1, nr_symbols+1):
    pw+=random.choice(symbols)

for n in range(1, nr_numbers+1):
    pw+=random.choice(numbers)
print(pw)"""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pw = []
for l in range(1, nr_letters+1):
    pw.append(random.choice(letters))

for s in range(1, nr_symbols+1):
    pw.append(random.choice(symbols))

for n in range(1, nr_numbers+1):
    pw.append(random.choice(numbers))
print(pw)

pwLength = nr_numbers+nr_symbols+nr_letters
randomPw = []
for order in range(0, pwLength-1):
    char = random.choice(pw)
    randomPw.append(char)
    pw.remove(char)

print(randomPw)

random.shuffle(randomPw)
print(randomPw)

