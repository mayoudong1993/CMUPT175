import random


#aim = random.randrange(1, 100)
#aim = random.choice(range(1, 100))
while (True):
    print("Game Session Starts")
    print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.")
    aim = random.randint(1, 99)
    print("Enter coins that add up to " + str(aim) + " cents, one per line.")
    a = "s"
    rest = aim
    while (rest > 0):
        a = input("Enter a valid coin value > ")
        if a == '':
            print("Session Ends!")
            break;
        elif (a != '1' and a != '5' and a != '10' and a != '25'):
            print('Invalid entry - Try again!')
        else:
            a = int(a)
            rest -= a
            #aim = aim - a
    print("Game Session Ends")
    print("Here is the outcome :")
    if (rest == 0):
        print("Success!")
    elif rest > 0:
        print("Failure - you only entered " + str(aim - rest) + " cents")
        print("You are short of", rest, "cents")
    elif rest < 0:
        print("Failure - you entered " + str(- rest + aim) + " cents")
        print("The amount exceeds " + str(aim) + " cents by " + str(-rest) + " cents")
    continuetoplay = input("Play another game session (y/n)?")
    if continuetoplay == 'n':
        print("Thanks for playing ... goodbye")
        break