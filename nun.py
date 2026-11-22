def roll():
    import random
    number = random.randint(1,6)
    if number == 1:
        print("You rolled 1")
    if number == 2:
        print("You rolled 2")
    if number == 3:
        print("You rolled 3")
    if number == 4:
        print("You rolled 4")
    if number == 5:
        print("You rolled 5")
    if number == 6:
        print("You rolled 6")
    return number

def luck():
    number = roll()
    if number == 1:
        print("Bruh")
                                                                                            
luck()
