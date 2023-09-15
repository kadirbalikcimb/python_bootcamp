import random

"""You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly 
like in the example e.g. Heads, not heads.
There are many ways of doing this. But to practice what we learnt in the last lesson, 
you should generate a random number, either 0 or 1. 
Then use that number to print out Heads or Tails."""

ranNum = random.randint(0,1)
print(ranNum)
if ranNum == 0:
    print("Tails")
else:
    print("Heads")