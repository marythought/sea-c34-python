# this is the file for donorletters code

# add note when safe_input.py completed

"""
Using all you've learned so far, complete your mailroom program
according to the pseudocode and flow chart you created last session.
use dicts where appropriate
see if you can use a dict to switch between the users selections
Try to use a dict and the .format() method to do the letter as one
big template – rather than building up a big string in parts.
For extra fun, see if you can use a file to preserve the donation list
and changes made to it while the program is running.
"""
MYDICT = {"mary": 50, "josh": 50, "cassie": 34}

print MYDICT


"""
def sendletter(name, dict):
    if name in MYDICT:
        # proceed
    elif name not in MYDICT:
        # add it

def mainmenu():
    action = raw_input("Would you like to 'SEND' a thank you note," +
                       " 'CREATE' a report, or 'QUIT'?")
    while action.upper() != "QUIT":
        if action.upper() == "SEND":
            action = raw_input("Please enter a full name, 'LIST' for options, or 'MENU' to go back")
            while action.upper() != "MENU":
                sendletter(action)
            else:
                mainmenu()
    else:
        exit()

"""


"""
if action == SEND:



        if name == “MENU”:

            go back to action prompt

        if name == “LIST”:

            print donorlist.keys #names

            name = raw_input(“Please enter a name from the list, or type a new one to add”)

        while name not in donorlist.keys:

            ask if they want to add the name y/n

                if y, add name to donorlist

                if no, ask for name again

        if name in donor list.keys:

            name.value = int(raw_input(ask for donation amount))

            while name.value is not an int,

                ask for name.value again

            add (name,value) to donorlist #how to add multiple donations to one user?

    def createletter(name,value):

        print “Dear %n, thank you for your generous donation of %v. We appreciate your support of our mission, which enables us to provide essential services to hundreds of Seattle families. Sincerely, do great inc.” %n name %v value

    createletter(name,value)

    name = MENU

if action == create:

    def createreport():

        sort donorlist by donation amount

        print donorlist.keys, sum(donorlist.values), count(donorlist.values) and average(donorlist.values)

    # return to main menu

    # action = raw_input(“Would you like to SEND a thank you note, CREATE a report, or QUIT?”)
"""
