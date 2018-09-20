dictionary = {
    'wallet' : 0,
    'walletTotal' : 0,
    'cost' : 0,
    'costTotal' : 0,
    'endSum' : 0,
    'gone' : "",
}

def shopping():
    dictionary['gone'] = input("Would you like to go out? 'y'es or 'n'o\n")
    if dictionary['gone'].lower() == "y":
        print("You go to your car and begin the journey.")
        out()
    elif dictionary['gone'].lower() == "n":
        print("You decide to stay home like an intelligent individual.\n")
    else:
        print("Please input a valid command.")
        shopping()

def out():
    print("You have arrived at the store.")
    while dictionary['gone'] == "y":
        x = input("\nWhat would you like to do now? 'a'tm, 'c'heckout, 'g'o home\n")
        if x.lower() == "a":
            aa = input("You walk to the nearest ATM. How much would you like "
                       "to withdraw?\nENTER A NUMBER\n")
            dictionary['wallet'] = dictionary['wallet'] + int(aa)
            dictionary['walletTotal'] = dictionary['walletTotal'] + int(aa)
            print("You now have $%d in your wallet."% (dictionary['wallet']))
        elif x.lower() == "c":
            dictionary['cost'] = input("You have arrived at the checkout "
                                       "counter. How much are you spending?"
                                       "\nENTER A NUMBER\n")
            dictionary['costTotal'] += int(dictionary['cost'])
            afford()
        elif x.lower() == "g":
            when_g()
        else:
            print("Please input a valid command.")

def afford():
    print("You're wallet is holding $%d, and you want to spend $%d."%
          (dictionary['wallet'], int(dictionary['cost'])))
    dictionary['wallet'] = dictionary['wallet'] - int(dictionary['cost'])
    print("You make the purchase.\n")
    if dictionary['wallet'] > 0:
        print("In your wallet remains $%d."% (dictionary['wallet']))
    elif dictionary['wallet'] < 0:
        print("You didn't have enough money in your wallet.\nYou will now owe "
              "$%d to your bank.\n"% (abs(dictionary['wallet'])))

def when_g():
    dictionary['endSum'] = dictionary['walletTotal'] - dictionary['costTotal']
    print("You decide to call it quits; It's time to go home.")
    dictionary['gone'] = "n"
    print("Today, you withdrew $%d from your account and spent a "
          "total of $%d."% (dictionary['walletTotal'], dictionary['costTotal']))
    if dictionary['endSum'] > 0:
        print("You go home happy, with money in your pocket.")
    elif dictionary['endSum'] < 0:
        print("Somehow, you managed to go into debt... $%d, to be "
              "exact. Never go shopping alone again."% (dictionary['endSum']))   
    print("This was the end dictionary:\n")
    for k, v in dictionary.items():
        print(k + ":", v)
    dictionary['wallet'] = 0
    dictionary['walletTotal'] = 0
    dictionary['cost'] = 0
    dictionary['costTotal'] = 0
    dictionary['endSum'] = 0
    dictionary['gone'] = ""
            
shopping()
