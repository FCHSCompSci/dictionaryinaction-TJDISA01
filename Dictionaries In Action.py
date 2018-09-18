dictionary = {
    'wallet' : 0,
    'cost' : 0,
    'gone' : "",
}

def shopping():
    dictionary['gone'] = input("Would you like to go out? 'y'es or 'n'o\n")
    if dictionary['gone'].lower() == "y":
        print("You go to your car and begin the journey.")
        out()
    elif dictionary['gone'].lower() == "n":
        print("You decide to stay home like an intelligent individual.\n")
        pass
    else:
        print("Please input a valid command.")
        shopping()

def out():
    print("You have arrived at the store.")
    while dictionary['gone'] == "y":
        x = input("\nWhat would you like to do now? 'a'tm, 'c'heckout, 'g'o home\n")
        if x.lower() == "a":
            aa = input("You walk to the nearest ATM. How much would you like to "
                       "withdraw?\nPUT IN A NUMBER\n")
            dictionary['wallet'] = dictionary['wallet'] + int(aa)
            print("You now have $%d in your wallet."% (dictionary['wallet']))
            
        elif x.lower() == "c":
            cc = input("You have arrived at the checkout counter. How much are "
                       "you spending?\nPUT IN A NUMBER\n")
            dictionary['cost'] -= int(cc)
            afford()
            
        elif x.lower() == "g": 
            print("You decide to call it quits; It's time to go home.")
            dictionary['gone'] = "n"
            print("Today you spent a total of $%d."% (dictionary['cost']))
            pass
        else:
            print("Please input a valid command.")
            out()

def afford():
    print("You're wallet is holding $%d, and you want to spend $%d."%
          (dictionary['wallet'], dictionary['cost']))
    if dictionary['wallet'] + dictionary['cost'] > 0:
        print("You can afford to make this purchase.")
        dictionary['wallet'] = dictionary['wallet'] - dictionary['cost']
    elif dictionary['wallet'] + dictionary['cost'] < 0:
        print("You cannot afford to make this purchase.")

shopping()
