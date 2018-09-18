dictionary: {
    'wallet' : 0,
    'cost' : 0,
    'gone' : maybe,
}
    
def shopping():
    maybe = input("Would you like to go out? 'y'es or 'n'o\n")
    if maybe.lower() == "y":
        print("You go to your car and begin the journey.")
        out()
    elif maybe.lower() == "n":
        print("You decide to stay home like an intelligent individual.")
    else:
        print("Please input a valid command.")
        shopping()

def out():
    print("You have arrived at the store.")
    while dictionary['gone'] == "y":
        x = input("What would you like to do? 'a'tm, 'c'heckout, 'g'o home")
        if x.lower() == "a":
            aa = input("You walk to the nearest ATM. How much would you like to "
                       "withdraw?\n")
            dictionary['wallet'] += aa
        elif x.lower() == "c":
            cc = input("You have arrived at the checkout counter. How much are "
                       "you spending?\n ")
            dictionary['cost'] -= cc
        elif x.lower() == "g": 
            print("You decide to call it quits; It's time to go home.")
            dictionary['gone'] = "n"


shopping()
