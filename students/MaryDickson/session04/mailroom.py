# this is the file for donorletters code

# add note when safe_input.py completed

d = {"Mary Dickson": [50, 100], "Joshua Diaz": [50], "Cassie Cat": [34]}


def createreport(dict):
    # print donorlist
    for key, value in dict.items():
        print "\n", key, value
        print "number of donations: " + str(len(value))
        print "sum of donations: $" + str(sum(value))
        print "average donation size: $" + str(sum(value) / len(value))


def add_donation(name, dict):
    """
    args: name, dict - name of donor to be added to a given dictionary (dict)

    returns: donation amount
    """
    print "You are about to add a donation for %s." % name
    print ("If this is correct, enter the amount below. "
           "Otherwise, type MENU to go back.\n")
    amount = raw_input("What is the amount of the donation? $")
    while type(amount) != int:
        try:
            amount = float(amount)
            amount = int(amount)
            return amount
        except:
            if amount == "MENU":
                mainmenu()
            amount = raw_input("Please enter a valid donation amount. "
                               "What is the amount of the donation? $")


def addamt(name, dict, amt):
    for key, value in dict.items():
        if key == name:
            dict[key] = dict[key] + [amt]
        elif name not in dict.keys():
            dict[name] = [amt]
    return dict
# SO BEAUTIFUL DO NOT BREAK.


def createletter(name, amount):
    return ("Dear %s, thank you for your donation" +
            " of $" + str(amount) + ".\n") % name


def sendletter(name, dict):
    """

    """
    amount = add_donation(name, dict)
    dict = addamt(name, dict, amount)
    letter = createletter(name, amount)
    return letter


def nameoptions(name, dict):
    """
    given a name, confirms correctness and calls functions to add them to d.

    returns: a dictionary
    """
    # name = name.capitalize()
    if name in dict.keys():
        proceed = raw_input(str(name) + " is in the donor database."
                            " Continue [Y]/[N]? :")
        if proceed.upper() == "Y":
            print sendletter(name, dict)
        else:
            mainmenu()
    else:
        proceed = raw_input(str(name) + " is not in the donor database."
                            " Add? [Y]/[N]? :")
        if proceed.upper() == "Y":
            print sendletter(name, dict)
        else:
            sendprogram()


def listdonors(dict):
    print dict.keys()
    sendprogram()


def sendprogram():
    """
    provides options for adding name to database and returns a name to use
    in subsequent functions
    """
    option = raw_input("Please enter a name, [LIST] for options," +
                       " or [MENU] to go back :")
    if option.upper() == "LIST":
        listdonors(d)

    elif option.upper() == "MENU":
        mainmenu()

    else:
        nameoptions(option, d)


def mainmenu():
    action = raw_input("Would you like to 'SEND' a thank you note," +
                       " 'CREATE' a report, or 'QUIT'? :")
    if action.upper() == "SEND" or action.upper() == "S":
        sendprogram()
        mainmenu()
    elif action.upper() == "CREATE" or action.upper() == "C":
        createreport(d)
        mainmenu()
    elif action.upper() == "QUIT" or action.upper() == "Q":
        exit()
    else:
        print "I don't understand that option, please choose again. "
        mainmenu()


mainmenu()
