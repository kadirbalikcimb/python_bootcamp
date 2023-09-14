print("Hello World!")
height = 120
if height >= 120:
    print("you are good to go")
    age = int(input("what is your age then?"))
    if  age < 0:
        print("this is not possible dude")
    elif age < 12:
        print("you should pay 5$")
    elif age <=18:
        print("you should pay 7$")
    else:
        print("you should pay 12$")
else:
    print("oops wait there!")