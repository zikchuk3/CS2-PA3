'''
A directory of food pantrys/banks/non profits (focus is in the DMV)
'''

#where should I use a dictionary? 
# dictionaries of the different cities/towns in each state?
# except for DC idk 
DC = {
    
}

MD = {
    "aberdeen": "city",
    "accident": "town",
    "annapolis": "city",
    "baltimore": "city",
    "barclay": "town",
    "barnesville": "town",
    "barton": "town",
    "bel air": "town",
    "berlin": "town",
    "betterton": "town",
    "bladensburg": "town",
    "boonsboro": "town",
    "bowie": "city",
    "brentwood": "town",
    "brookeville": "town",
    "brunswick": "city",
    "burkittsville": "town",
    "cambridge": "city",
    "capitol heights": "town",
    "cecilton": "town",
    "centreville": "town",
    "charlestown": "town",
    "chesapeake beach": "town",
    "chesapeake city": "town",
    "chevy chase": "town",
    "chevy chase view": "town",
    "church creek": "town",
    "church hill": "town",
    "chestertown": "town",
    "college park": "city",
    "cottage city": "town",
    "crisfield": "city",
    "cumberland": "city",
    "delmar": "town",
    "denton": "town",
    "district heights": "city",
    "eagle harbor": "town",
    "east new market": "town",
    "easton": "town",
    "edmonston": "town",
    "elkton": "town",
    "emmitsburg": "town",
    "fairmount heights": "town",
    "federalsburg": "town",
    "forest heights": "town",
    "frederick": "city",
    "friendsville": "town",
    "frostburg": "city",
    "funkstown": "town",
    "gaithersburg": "city",
    "galena": "town",
    "garrett park": "town",
    "glen echo": "town",
    "glenarden": "city",
    "goldsboro": "town",
    "grantsville": "town",
    "greenbelt": "city",
    "greensboro": "town",
    "hagerstown": "city",
    "hampstead": "town",
    "hancock": "town",
    "havre de grace": "city",
    "hebron": "town",
    "henderson": "town",
    "highland beach": "town",
    "hillsboro": "town",
    "hurlock": "town",
    "hyattsville": "city",
    "indian head": "town",
    "keedysville": "town",
    "kensington": "town",
    "kitzmiller": "town",
    "la plata": "town",
    "landover hills": "town",
    "laurel": "city",
    "laytonsville": "town",
    "leonardtown": "town",
    "loch lynn heights": "town",
    "lonaconing": "town",
    "manchester": "town",
    "mardela springs": "town",
    "marydel": "town",
    "middletown": "town",
    "midland": "town",
    "millington": "town",
    "morningside": "town",
    "mount airy": "town",
    "mount rainier": "city",
    "myersville": "town",
    "new carrollton": "city",
    "new market": "town",
    "new windsor": "town",
    "north beach": "town",
    "north brentwood": "town",
    "oakland": "town",
    "ocean city": "town",
    "oxford": "town",
    "perryville": "town",
    "pocomoke city": "city",
    "poolesville": "town",
    "port deposit": "town",
    "princess anne": "town",
    "queen anne": "town",
    "queenstown": "town",
    "ridgely": "town",
    "rising sun": "town",
    "riverdale park": "town",
    "rock hall": "town",
    "rockville": "city",
    "rosemont": "town",
    "salisbury": "city",
    "seat pleasant": "city",
    "secretary": "town",
    "sharpsburg": "town",
    "sharptown": "town",
    "smithsburg": "town",
    "snow hill": "town",
    "somerset": "town",
    "st michaels": "town",
    "sudlersville": "town",
    "sykesville": "town",
    "takoma park": "city",
    "taneytown": "town",
    "templeville": "town",
    "thurmont": "town",
    "trappe": "town",
    "union bridge": "town",
    "university park": "town",
    "upper marlboro": "town",
    "vienna": "town",
    "walkersville": "town",
    "washington grove": "town",
    "westminster": "city",
    "willards": "town",
    "williamsport": "town",
    "woodsboro": "town"
}

VA = {
    "alexandria": "city",
    "bristol": "city",
    "Buena Vista": "city",
    "Charlottesville": "city",
    "Chesapeake": "city",
    "Colonial Heights": "city",
    "Covington": "city",
    "Danville": "city",
    "Emporia": "city",
    "Fairfax": "city",
    "Falls Church": "city",
    "Franklin": "city",
    "Fredericksburg": "city",
    "Galax": "city",
    "Hampton": "city",
    "Harrisonburg": "city",
    "Hopewell": "city",
    "Lexington": "city",
    "Lynchburg": "city",
    "Manassas": "city",
    "Manassas Park": "city",
    "Martinsville": "city",
    "Newport News": "city",
    "Norfolk": "city",
    "Norton": "city",
    "Petersburg": "city",
    "Poquoson": "city",
    "Portsmouth": "city",
    "Radford": "city",
    "Richmond": "city",
    "Roanoke": "city",
    "Salem": "city",
    "Staunton": "city",
    "Suffolk": "city",
    "Virginia Beach": "city",
    "Waynesboro": "city",
    "Williamsburg": "city",
    "Winchester": "city"
}

# displays files of places + info based on user input
def display():
    print("displays user input of places near them")
    # different files for D M and V

#username so that each person who uses can make their own list
def user():
    print("enter your name")

#if the user wants to add to their list
def add_list():
    print("added to your list")
    # added to a seperate file

# for error handling
def error():
    print("error")

#what the user can input in main
def menu():
    print("---- What will you choose? ----")
    print("1. Washington DC")
    print("2. Maryland")
    print("3. Virginia")
    print("4. Enter your city")
    print("5. Exit")

#main function
def main():
    # error handling lists
    choices = ["1", "2", "3", "4", "Washington DC", "DC", "Maryland", "MD", "Virginia", "VA"]
    stop_choices = ["5", "Exit"]


    # intro
    print("Hello. This is the FoodDirectory (might change name), where you can learn about for any Food Bank, Food Pantry, or non-profit that offers meals.")
    print("All you have to do is type in your state or city, and I will present to you different places and information.")
    print("I currently only know the DMV. Sorry :( ")
    print()

    print("You can either choose a state and look at the cities, or enter your own city.")
    print()
    menu()
    choice = input()
    while choice not in stop_choices:
        if choice == "1" or choice == "Washington DC" or choice == "DC":
            print("Here are the places in DC:")
            print(DC)
        elif choice == "2" or choice == "Maryland" or choice == "MD":
            print("Here are the cities in Maryland:")
            print(MD)
        elif choice == "3" or choice == "Virginia" or choice == "VA":
            print("Here are the cities in Virgnia:")
            print(VA)
        elif choice == "4":
            city = input("Enter your city.")
        else:
            error()
        print()
        menu()
        choice = input()



main()