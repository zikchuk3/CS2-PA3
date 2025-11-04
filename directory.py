'''
A directory of food pantrys/banks/non profits (focus is in the DMV)
'''
import json #for json file
# json files are formatted in an easier way then dictionaries 
with open("food_banks.json", "r") as file:
    info = json.load(file)


# for error handling
def error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

# directory funcs for D M and V when user chooses from menu
def dc_directory():
    city = "Washington DC"
    places = info[city]

    for i, place in enumerate(places, start = 1):
        print(f"{i}. {place['name']} - {place['address']}")

    choice = input("Enter the number of the place you would like to learn about: ")

    #isdigit() returns True if all characters are digits
    # if the choice is a digit and 1 <= user choice <= number of places there
    if choice.isdigit() and 1 <= int(choice) <= len(places):
        learn(city, int(choice) - 1) # -1 is for the position thing
    else:
        error()

def md_directory():
    # list just ot display info
    MD = ['baltimore', 'silver spring', 'rockville', 'bathesda', 'columbia', 'germantown']
    print("Here are the cities in Maryland this directory has: ")
    print(MD)
    city = input("Choose a city you want to explore: ")
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        choice = input("Enter the number of the place you would you like to learn about: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        else:
            error()
    else:
        print("Sorry, I don't have that city yet. :(")
        city = input("Choose a city you want to explore: ")

def va_directory():
    # list just ot display info
    VA = ['richmond', 'arlington', 'charlottesville', 'alexandria', 'falls church', 'hayfeild']
    print("Here are the cities in Virgnia this directory has: ")
    print(VA)
    city = input("Choose a city you want to explore: ")
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        choice = input("Enter the number of the place you would you like to learn about: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        else:
            error()
    else:
        print("Sorry, I don't have that city yet. :(")
        city = input("Choose a city you want to explore: ")

# directory func if user knows city and just wants to type this in
def all_directory(city):
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        choice = input("Enter the number of the place you would you like to learn about: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        else:
            error()
    else:
        print("Sorry, I don't have that city yet. :(")

#to learn about the certain food bank/pantry/non profit
def learn(city, index):
    place = info[city][index]

    print()
    print(f"---- {place['name']} ----")
    print(f"Address: {place["address"]}")
    print()
    print(f"Hours: {place['hours']}")
    print(f"Phone: {place['phone']}")
    print(f"Summary: {place['summary']}")
    print(f"Website: {place['website']}")
    print()

    save_choices = ["yes", "y"]
    back_choices = ["n", "no"]
    user_input = input("Would you like to bookmark this place? (y)es or (n)o: ")
    if user_input in save_choices:
        add_list(place)
    elif user_input in back_choices:
        return
    else:
        error()
        user_input = input("Would you like to bookmark this place? (y)es or (n)o: ")


#if the user wants to add to bookmark place
def add_list(bookmarked_place):
    # first they name their list (file)
    name_input = input("What is your name so I can add this to your bookmarks?: ")
    user_file = name_input+".txt" #.txt by default

    with open(user_file, "w") as f:
        f.write(f"{bookmarked_place}")
    with open("bookmarks.txt", "a") as g:
        g.write(user_file + "\n")

    print("Okay! Your bookmark has been saved! View your bookmarks throught the menu")

# to show bookmarks
def show_list():
    try:
        with open("bookmarks.txt", "r") as g:
            bookmarks = [line.strip() for line in g.readlines() if line.strip()]
    except FileNotFoundError:
        print("No bookmark list found. Create a bookmark when you learn about a place. ")
        return
    # if the bookmarks.txt exists and there is nothing in it
    if not bookmarks:
        print("There are no bookmarks found. Create one when you learn about a place. ")
        return

    print(" ---- BOOKMARKS ----")
    for i, bookmark in enumerate(bookmarks, 1):
        print(f"{i}. {bookmark}")
    
    choice = input("Enter the number of your bookmark list so you can see your bookmarks or 'b' to go back.")
    if choice.lower() == "b":
        return
    try:
        choice = int(choice)
        1 <= choice <= len(bookmarks)
        chosen_bookmark = bookmarks[choice -1]
        with open(chosen_bookmark, "r") as f:
            f.readlines()
    except ValueError:
        print("Please enter a number shown.")


#what the user can input in main
def menu():
    print("---- What will you choose? ----")
    print("1. Washington DC")
    print("2. Browse cities in Maryland")
    print("3. Browse cities in Virginia")
    print("4. Enter your city")
    print("5. Exit")

#main function
def main():
    # error handling lists
    choices = ["1", "2", "3", "4", "Washington DC", "DC", "Maryland", "MD", "Virginia", "VA"]
    stop_choices = ["5", "Exit"]


    # intro
    print("Hello. This is FoodDirectory (might change name), a place where you can learn about any Food Bank, Food Pantry, or non-profit that offers meals.")
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
            dc_directory()
        elif choice == "2" or choice == "Maryland" or choice == "MD":
            md_directory()
        elif choice == "3" or choice == "Virginia" or choice == "VA":
            va_directory()
        elif choice == "4":
            city = input("Enter your city: ")
            all_directory(city)
        else:
            error()
        print()
        menu()
        choice = input()



main()