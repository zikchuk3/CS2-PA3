'''
A directory of food pantrys/banks/non profits (focus is in the DMV)
'''
import time
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
    city = "washington dc"
    places = info[city]

    for i, place in enumerate(places, start = 1):
        print(f"{i}. {place['name']} - {place['address']}")
    print()
    choice = input("Enter the number of the place you would like to learn about or 'exit' to return to go back to the menu: ").strip()

    #isdigit() returns True if all characters are digits
    # if the choice is a digit and 1 <= user choice <= number of places there
    if choice.isdigit() and 1 <= int(choice) <= len(places):
        learn(city, int(choice) - 1) # -1 is for the position thing
    elif choice == "exit":
        return
    else:
        error()
        dc_directory()

def md_directory():
    # list just ot display info
    MD = ['baltimore', 'silver spring', 'rockville', 'bathesda', 'college park', 'gaithersburg']
    print("Here are the cities in Maryland this directory has: ")
    print(MD)
    print()
    city = input("Choose a city you want to explore or 'exit' to go back to the menu: ").lower().strip()
    print()
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        print()
        choice = input("Enter the number of the place you would you like to learn about: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        else:
            error()
            md_directory()
    elif city == "exit":
        return
    else:
        print("Sorry, I don't have that city yet. :(")
        md_directory()

def va_directory():
    # list just ot display info
    VA = ['richmond', 'arlington', 'charlottesville', 'alexandria', 'falls church', 'fairfax']
    print("Here are the cities in Virgnia this directory has: ")
    print(VA)
    print()
    city = input("Choose a city you want to explore or 'exit' to go back to the menu: ").lower().strip()
    print()
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        print()
        choice = input("Enter the number of the place you would you like to learn about: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        else:
            error()
            va_directory()
    elif city == "exit":
        return
    else:
        print("Sorry, I don't have that city yet. :(")
        va_directory()

# directory func if user knows city and just wants to type this in
def all_directory(city):
    if city in info:
        places = info[city]
        for i, place in enumerate(places, start=1):
            print(f"{i}. {place['name']} - {place['address']}")
        print()
        choice = input("Enter the number of the place you would you like to learn about or 'exit' to go back to the menu: ")
        if choice.isdigit() and 1 <= int(choice) <= len(places):
            learn(city, int(choice) - 1)
        elif choice == "exit":
            return
        else:
            error()
    else:
        print("Sorry, I don't have that city yet. :(")

#to learn about the certain food bank/pantry/non profit
def learn(city, index):
    place = info[city][index]

    #printing things in the json file
    time.sleep(1)
    print()
    print(f"---- {place['name']} ----")
    print(f"Address: {place["address"]}")
    print()
    print(f"Hours: {place['hours']}")
    print(f"Phone: {place['phone']}")
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
    time.sleep(0.5)
    name_input = input("What is your name so I can add this to your bookmarks?: ")
    # to check if that file name already exists so it doesnt add to bookmarks.txt again
    name_check = name_input+".txt"
    x = open("bookmarks.txt", "r")
    check = x.readlines()
    if name_check+"\n" in check:
        time.sleep(1)
        print("Added bookmark to your existing bookmark list.")
        with open(name_check, "a") as f:
            f.write(f" \n Name: {bookmarked_place['name']} \n")
            f.write(f"Address: {bookmarked_place['address']} \n")
            f.write(f"Hours: {bookmarked_place['hours']} \n")
            f.write(f"Phone: {bookmarked_place['phone']} \n")
            f.write(f"Website: {bookmarked_place['website']} \n")
    # if file doesnt exist already
    else:
        time.sleep(0.3)
        print("Creating a new bookmark list...")
        time.sleep(1)
        user_file = name_input+".txt" #.txt by default
        with open(user_file, "a") as f:
            f.write(f" \n Name: {bookmarked_place['name']} \n")
            f.write(f"Address: {bookmarked_place['address']} \n")
            f.write(f"Hours: {bookmarked_place['hours']} \n")
            f.write(f"Phone: {bookmarked_place['phone']} \n")
            f.write(f"Website: {bookmarked_place['website']} \n")

        with open("bookmarks.txt", "a") as g:
            g.write(user_file + "\n")
            print("Okay! Your bookmark has been saved! View your bookmarks throught the menu")

# to show bookmarks
def show_list():
    try:
        # read the bookmarks list if theres anything in it
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
    
    print()
    choice = input("Enter the number of your bookmark list so you can see your bookmarks or 'b' to go back: ")
    if choice.lower() == "b":
        return
    try:
        choice = int(choice)
        # if not in this range
        if not (1 <= choice <= len(bookmarks)):
            print("Please enter a number shown.")
            print()
            # calls show list again then returns
            show_list()
            return
        
        chosen_bookmark = bookmarks[choice -1]
        time.sleep(1)
        with open(chosen_bookmark, "r") as f:
            inside = f.readlines()
            # join is to put the lines back in a string using a space as a separater 
            print("\n" + "".join(inside) + "\n")

            #was going to be to delete a certain thing in your bookmark list but ran out of time
            '''
            save_choices = ["yes", "y"]
            back_choices = ["n", "no"]
            delete_choice = input("Is there any bookmark you would like to delete? (y)es or (n)o: ")
            if delete_choice in save_choices:
                del_place = input("Which bookmark would you like to delete? (type the name of the place): ")
                if del_place in inside:
                    delete_list(chosen_bookmark, del_place)
            elif delete_choice in back_choices:
                return
            else:
                error()
                delete_choice = input("Is there any bookmark you would like to delete? (y)es or (n)o: ")'''
    except ValueError:
        error()
        print("Please enter a valid number.")


# was going to add this but it would take to long
'''
#so bassically, make a dictionary with the info and then overwwrite it into the json? when you append certain value
# to clear bookmark in bookmark list (trying to make it so it is a certain bookmark instead of whole list)
def delete_list(bookmark_list, bookmark_place):
    #dictionary of the foodbanks from the json
    dictionary = {
        "Capital Area Food Bank": {
            "address": "4900 Puerto Rico Ave NE, Washington, DC 20017",
            "hours": "Mon-Fri 9am-3pm",
            "phone": "(202) 644-9800",
            "website": "https://www.capitalareafoodbank.org/"
        },
        "Martha's Table at the Commons": {
            "address": "2375 Elvans Rd SE, Washington, DC 20020",
            "hours": "Mon-Fri 9am-4pm",
            "phone": "(202) 328-6608",
            "website": "https://marthastable.org/"
        },
        "Martha's Table at the Maycroft": {
            "address": "1474 Columbia Rd NW, Washington, DC 20009",
            "hours": "Mon-Thurs 9am-5pm, Fri 9am-12pm",
            "phone": "(202) 328-6608",
            "website": "https://marthastable.org/"
        },
        "Bread for the City": {
            "address": "1525 7th St NW, Washington, DC 20001",
            "hours": "Mon-Thurs 9am-3pm",
            "phone": "(202) 265-2400",
            "website": "https://breadforthecity.org/"
        },
        "Maryland Food Bank": {
            "address": "2200 Halethorpe Farms Rd, Baltimore, MD 21227",
            "hours": "Mon-Fri 8am-4:30pm",
            "phone": "(410) 737-8282",
            "website": "https://mdfoodbank.org"
        },
        "Beans & Bread": {
            "address": "400 S Bond St, Baltimore, MD 21231",
            "hours": "Mon-Fri 9am-2pm",
            "phone": "(410) 732-1892",
            "website": "http://www.vincentbaltimore.org/get-help"
        },
        "Franciscan Center": {
            "address": "101 W 23rd St, Baltimore, MD 21218",
            "hours": "Mon+Thurs+Fri 10am-1pm, Tues+Wed 10am-1pm, 5:30-7pm",
            "phone": "(410) 467-5340",
            "website": "http://fcbmore.org/"
        },
        "The Food Project": {
            "address": "424 S Pulaski St, Baltimore, MD 21223",
            "hours": "Mon-Fri 10am-2pm, Sat 9am-12pm",
            "phone": "(443) 690-1694",
            "website": "http://www.uempowerofmd.org/"
        },
        "Shepherd's Table Inc.": {
            "address": "8106 Georgia Ave, Silver Spring, MD 20910",
            "hours": "Mon-Fri 7:30am-7pm, Sat+Sun 10am-7pm",
            "phone": "(301) 585-6463",
            "website": "http://www.shepherdstable.org/"
        },
        "Manna Food Center Market": {
            "address": "12301 Old Columbia Pike, Silver Spring, MD 20904",
            "hours": "Mon-Thurs 8:30am-4pm, Fri 8am-3pm",
            "phone": "(301) 424-1130",
            "website": "http://www.mannafood.org/"
        },
        "Mid-County United Ministries (MUM)": {
            "address": "11002 Veirs Mill Rd Suite 710, Silver Spring, MD 20902",
            "hours": "Tues-Thurs 9am-4pm",
            "phone": "(301) 929-8675",
            "website": "https://mumhelp.org/"
        },
        "Rainbow Community Development Center": {
            "address": "2120 Industrial Pkwy A, Silver Spring, MD 20904",
            "hours": "Mon-Fri 10am-6pm",
            "phone": "(301) 625-2561",
            "website": "http://rainbowcdc.org/"
        },
        "Nourish Now": {
            "address": "397 E Gude Dr, Rockville, MD 20850",
            "hours": "Mon-Fri 9:30am-4:30pm",
            "phone": "(301) 330-0222",
            "website": "http://nourishnow.org/"
        },
        "Interfaith Works Essential Needs Center": {
            "address": "751 Twinbrook Pkwy # 8, Rockville, MD 20851",
            "hours": "Tues-Fri 8:30am-4pm, Sat 8:30am-1pm",
            "phone": "(301) 424-3796",
            "website": "http://iworksmc.org/"
        },
        "Manna Food Center": {
            "address": "9311 Gaither Rd, Gaithersburg, MD 20877",
            "hours": "Mon-Fri 8am-2pm",
            "phone": "(301) 424-1130",
            "website": "http://www.mannafood.org/"
        },
        "Gaithersburg HELP Pantry": {
            "address": "301 Muddy Branch Rd, Gaithersburg, MD 20878",
            "hours": "N/A",
            "phone": "(301) 216-2510",
            "website": "http://gaithersburghelp.org/"
        },
        "So What Else Inc.": {
            "address": "4924 Wyaconda Rd, North Bethesda, MD 20852",
            "hours": "Mon+Fri 8:30am-4pm, Tues-Thurs 8:30am-4:30pm, Sat 7am-1pm",
            "phone": "(301) 887-3808",
            "website": "https://www.sowhatelse.org/"
        },
        "Montgomery County Food Council": {
            "address": "4825 Cordell Ave 2nd Floor, Bethesda, MD 20814",
            "hours": "N/A",
            "phone": "(301) 664-4010",
            "website": "http://mocofoodcouncil.org/contact-us-2/"
        },
        "Nourishing Bethesda": {
            "address": "10319 Westlake Drive Suite 262, Bethesda, MD 20817",
            "hours": "N/A",
            "phone": "(301) 664-4630",
            "website": "https://www.nourishingbethesda.org/"
        },
        "Bethesda Cares-First Baptist Church": {
            "address": "5033 Wilson Lane, Bethesda, MD 20814",
            "hours": "Mon-Fri 1st to the 15th of the month, 1pm-2pm",
            "phone": "(301) 907-9244",
            "website": "http://www.bethesdacares.org/"
        },
        "UMD Campus Pantry": {
            "address": "South Campus Dining Hall, 7093 Preinkert Dr, College Park, MD 20740",
            "hours": "Mon-Fri 10am-5pm (UMD students only)",
            "phone": "(301) 405-9579",
            "website": "https://dining.umd.edu/sustainability/campus-pantry"
        },
        "College Park Community Food Bank": {
            "address": "9704 Rhode Island Ave, College Park, MD",
            "hours": "Sat 9:30-11am",
            "phone": "See contact page",
            "website": "http://www.collegeparkfoodbank.com/"
        },
        "Saint Mark The Evangelist Catholic Church - Food Pantry": {
            "address": "7501 Adelphi Rd, Hyattsville, MD 20783",
            "hours": "Tues 10am-12pm",
            "phone": "(301) 779-2763",
            "website": "N/A"
        },
        "Congregations United For Compassion & Empowerment (Soup Kitchen)": {
            "address": "6800 Adelphi Rd, Hyattsville, MD 20782",
            "hours": "Tues+Thurs 1-5pm",
            "phone": "(301) 922-7054",
            "website": "https://www.congregationsunited.org/"
        },
        "Community Hope Center (Gaithersburg Hub) Food Pantry": {
            "address": "13 Firstfield Rd Suite 100, Gaithersburg, MD 20878",
            "hours": "Tues+Thurs 10am-4:30pm, Fri 1-4pm, 1st Sat 9:45am-12pm",
            "phone": "(240) 229-9642",
            "website": "https://senecacreek.org/get-assistance/"
        },
        "Saint Martin of Tours Food Pantry": {
            "address": "201 S Frederick Ave, Gaithersburg, MD 20877",
            "hours": "Mon 6:30-11:30am",
            "phone": "(301) 990-3203",
            "website": "https://www.stmartinsweb.org/st-martin-s-pantry"
        },
        "Feed More": {
            "address": "8020 Villa Park Dr, Richmond, VA 23228",
            "hours": "Mon-Fri 8am-4pm",
            "phone": "(804) 521-2500",
            "website": "https://www.feedmore.org/"
        },
        "Liberation Church & Outreach Center": {
            "address": "5501 Midlothian Tpke, Richmond, VA 23224",
            "hours": "Tues+Thurs 2-4pm",
            "phone": "(804) 651-3067",
            "website": "N/A"
        },
        "Church of the Holy Comforter Food Pantry": {
            "address": "4819 Monument Ave, Richmond, VA 23226",
            "hours": "Tues 5:30-6:30pm, Sat 11am-12pm",
            "phone": "(804) 355-3251",
            "website": "https://feedmore.org/agency/church-of-the-holy-comforter/"
        },
        "Lamb's Basket": {
            "address": "8419 Oakview Ave, Henrico, VA 23228",
            "hours": "Tues+Thurs 10am-12pm",
            "phone": "(804) 565-8007",
            "website": "http://www.lambsbasket.org/"
        },
        "Arlington Food Assistance Center (AFAC)": {
            "address": "2708 S Nelson St, Arlington, VA 22206",
            "hours": "Mon+Wed+Fri 9am-1pm, Tues+Thurs 9am-1pm + 6-7pm, Sat 8:30am-12:30pm",
            "phone": "(703) 845-8486",
            "website": "https://afac.org/"
        },
        "Salvation Army Food Pantry (Arlington)": {
            "address": "518 S Glebe Rd, Arlington, VA 22204",
            "hours": "N/A",
            "phone": "(703) 979-3380",
            "website": "https://www.salvationarmyusa.org/usn/cure-hunger/"
        },
        "The Little Yellow Free Pantry": {
            "address": "203 S Fillmore St, Arlington, VA 22204",
            "hours": "24/7",
            "phone": "N/A",
            "website": "https://mapping.littlefreepantry.org/pantry/3084"
        },
        "Our Lady Queen Of Peace Church - Food Distribution Center": {
            "address": "2700 19th St S, Arlington, VA 22201",
            "hours": "Wed 9am-11:30am",
            "phone": "(703) 979-5580",
            "website": "https://www.ourladyqueenofpeace.org/food-pantry.html"
        },
        "Food For Others": {
            "address": "2938 Prosperity Ave, Fairfax, VA 22031",
            "hours": "Mon-Fri 9:30am-5pm",
            "phone": "(703) 207-9173",
            "website": "http://www.foodforothers.org/"
        },
        "Free Little Food Pantry (Fairfax)": {
            "address": "9019 Little River Turnpike, Fairfax, VA 22031",
            "hours": "24/7",
            "phone": "N/A",
            "website": "https://www.littlefreepantry.org/"
        },
        "Blessing Box (Fairfax)": {
            "address": "Van Dyck Park, 3720 Old Lee Hwy, Fairfax, VA 22030",
            "hours": "24/7",
            "phone": "(703) 273-7586",
            "website": "N/A"
        },
        "Cornerstones Food Pantry": {
            "address": "11484 Washington Plaza W #120, Reston, VA 20190",
            "hours": "Mon-Thurs 8:30am-4pm, Fri 8:30am-1pm",
            "phone": "(571) 323-1400",
            "website": "https://www.cornerstonesva.org/"
        },
        "Catholic Charities Christ House Food Pantry": {
            "address": "4725-A Eisenhower Ave, Alexandria, VA 22304",
            "hours": "Wed+Thurs 9am-1pm",
            "phone": "(703) 548-4227",
            "website": "https://www.ccda.net/need-help/food/food-pantries/alexandria-food-pantry/"
        },
        "ALIVE! Warehouse": {
            "address": "801 S Payne St, Alexandria, VA 22314",
            "hours": "Mon-Fri 10am-4pm, Sat 9am-12pm",
            "phone": "(703) 837-9300",
            "website": "https://www.alive-inc.org/food-program-in-alexandria-virginia/"
        },
        "United Community": {
            "address": "7511 Fordson Rd, Alexandria, VA 22306",
            "hours": "Mon-Fri 9am-5pm",
            "phone": "(703) 768-7106",
            "website": "http://www.unitedcommunity.org/"
        },
        "Koinonia Foundation Inc": {
            "address": "6037 Franconia Rd, Alexandria, VA 22310",
            "hours": "Mon-Wed+Fri 9am-12:30pm, Mon 4-7:30pm, Thurs 9am-4:30pm",
            "phone": "(703) 971-1991",
            "website": "http://koinoniacares.org/"
        },
        "Columbia Baptist Church Center For Missions": {
            "address": "103 W Columbia St, Falls Church, VA 22046",
            "hours": "Sat 9-10:30am",
            "phone": "(703) 534-5700",
            "website": "https://columbia.church/join-the-mission/local/food-pantry/"
        },
        "Falls Church Community Service Council": {
            "address": "7416 Arlington Blvd, Falls Church, VA 22042",
            "hours": "Mon-Fri 8am-4:30pm",
            "phone": "(703) 237-2562",
            "website": "https://fcswecare.org/"
        },
        "Blue Ridge Area Food Bank - Eastern Region": {
            "address": "1207 Harris St, Charlottesville, VA 22903",
            "hours": "Mon-Fri 8am-4:30pm",
            "phone": "(434) 296-3663",
            "website": "https://www.brafb.org/"
        },
        "Loaves & Fishes Food Pantry": {
            "address": "2050 Lambs Rd, Charlottesville, VA 22901",
            "hours": "Tues 4-7pm, Wed 3-4pm, Thurs 6:30-8:30pm, Sat 10am-12pm",
            "phone": "(434) 996-7868",
            "website": "https://cvillefoodpantry.org/"
        },
        "Emergency Food Network": {
            "address": "900 Harris St, Charlottesville, VA 22902",
            "hours": "Mon+Wed+Fri+Sat 9am-12pm, 1:30-3:30pm",
            "phone": "(434) 979-9180",
            "website": "http://emergencyfoodnetwork.org/"
        },
        "Buck Mountain Episcopal Food Distribution Center": {
            "address": "4133 Earlysville Rd, Earlysville, VA 22936",
            "hours": "2nd and 4th Wednesday monthly, 3-5pm",
            "phone": "(434) 973-2054",
            "website": "https://buckmountainchurch.org/earlysville-food-pantry/"
        }
    }

    place = bookmark_place
    # open the bookmark list
    with open(f"{bookmark_list}", "r") as g:
        # check if the place the person inputed is in the list
        bookmarks = [line.strip() for line in g.readlines() if f"{place}" in line]
    if not bookmarks:
        print("There is no bookmark with that place in this list.")
        return
    else:
        print()
    
    #print(f"Succesfully deleted {place} from your list")'''

# MENU
# used DICTIONARY here
def menu():
    menu = {
        "1": "Washington DC",
        "2": "Browse cities in Maryland",
        "3": "Browse cities in Virginia",
        "4": "Type in your city",
        "5": "Show bookmarks",
        "6": "Exit"
    }

    print("---- What will you choose? ----")
    for key, value in menu.items():
        print(f"{key}. {value}")

#main function
def main():
    # error handling lists
    choices = ["1", "2", "3", "4", "5", "Washington DC", "DC", "Maryland", "MD", "Virginia", "VA","city", "show bookmarks", "bookmarks", "show"]
    stop_choices = ["6", "Exit"]

    print()
    print()
    # intro
    time.sleep(0.5)
    print("Hello. This is FoodDirectory, a place where you can learn about any Food Bank, Food Pantry, or non-profit that offers meals.")
    time.sleep(0.5)
    print("All you have to do is to select your state or city, and I will present to you different places and information.")
    time.sleep(0.5)
    print("I currently only know a few cities in the DMV area. Sorry :( ")
    print()
    time.sleep(1)

    print("You can either choose a state and look at the cities, or enter your own city.")
    print()
    time.sleep(0.5)
    menu()
    choice = input()
    print()
    while choice not in stop_choices:
        if choice == "1" or choice == "Washington DC" or choice == "DC":
            time.sleep(0.7)
            print("Here are the places in DC:")
            dc_directory()
        elif choice == "2" or choice == "Maryland" or choice == "MD":
            time.sleep(0.7)
            md_directory()
        elif choice == "3" or choice == "Virginia" or choice == "VA":
            time.sleep(0.7)
            va_directory()
        elif choice == "4" or choice == "city":
            time.sleep(0.7)
            city = input("Type in your city: ").lower()
            all_directory(city)
        elif choice == "5" or choice == "show bookmarks" or choice == "show" or choice == "bookmarks":
            time.sleep(0.7)
            show_list()
        else:
            error()
        print()
        time.sleep(0.5)
        menu()
        choice = input()

    time.sleep(0.5)
    print("Goodbye! ")

main()