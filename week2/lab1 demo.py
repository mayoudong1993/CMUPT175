import random

while (True):
    target = random.randint(1, 99)
    # random.randrange(1, 100)
    remaining = target
    print("Game Session Starts")
    print("Enter coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.")
    print("Enter coins that add up to", target, "cents, one per line.")
    while (remaining > 0):
        coins = input("Enter a valid coin value > ")
        if coins == "":
            break
        elif coins != "1" and coins != "5" and coins != "10" and coins != "25":
            print("Invalid entry - Try again!")
            continue
        else:
            coins = int(coins)
        remaining -= coins
        # remaining = remaining - coins

    print("Session Ends! \n Game Session Ends \n Here is the outcome :")

    if (remaining > 0):
        print("Failure - you only entered", target - remaining, "cents")
        print("You are short of", remaining, "cents")
    elif (remaining < 0):
        print("Failure - you entered", target - remaining, "cents")
        print("The amount exceeds", target, "cents by", -remaining, "cents")
    elif (remaining == 0):
        print("Success!")
