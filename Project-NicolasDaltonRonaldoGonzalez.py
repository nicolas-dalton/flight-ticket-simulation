# Name: Nick Dalton & Ronaldo Gonzalez
# Date: 12/2/19
# Course: COSC 2316 Fall 2019 (Dr. Shebaro)
# Program Description: Flight Purchase Program

######### Algorithm/Psuedocode ########
# 1. Open the input file, and create a loop that will read each line and each word is an element in its list
# 2. Create a List of lists each element of is a date with its flights
# 3. Create a dictionary that will put have keys as dates and values as the flights for the dates
# 4. Take user input for a destination and find all the flights with its information that has the destination
# 5. Display menu where it would give the options to have selective sorting
# 6. First option is to display the flights
# 7. Following 2 options is to sort from the earliest flight date to the latest and vice versa
# 7.1 In order to do this we would loop over each element and check the index that represents the dates and sort it.
# 8. The following 2 options is to sort the cheapest to expensive and vice versa
#  8.1 In order to do this we would loop over each element and check the index that represents the price and sort it.
# 9. Following 2 options is to sort from the earliest flight time to the latest and vice versa
# 9.1 In order to do this we would loop over each element and check the index that represents the times and sort it.
# 10. Following option is to purchase flight
# 10.1 User would select an ID of a flight and loop over each flight to see the ID matched with the flight, with a match user is asked questions and confirmation
# 10.2 It would print the output of the flight and information of the user in text file
# 11. The last option is the exit of the program

# Fuction Description: Open text file, that contains dates and flight information
# Precondition: Calls text file
# Postcondition: File that contains flights information
def openFile():
    inputFile = open("input.txt", "r")
    lines = inputFile.read().splitlines()
    lines= [lines[x:x+46] for x in range(0, len(lines),46)]
    flightsDic={}
    datesList=[]
    flightsForDates=[]
    justFlights=[]
    for i in range(len(lines)):
        datesList.append(lines[i][0])
        del lines[i][0]
    for i in range(len(lines)):
        flightsForDates.append([lines[i][x:x + 9] for x in range(0, len(lines[i]), 9)])
    flightsDic = {k: v for k, v in zip(datesList, flightsForDates)}
    return flightsDic
# Fuction Description:  Option for user to view sorted flights through earliest dates
# Precondition: User selects a valid city
# Postcondition: List of the earliest dates of the selected city
def earliestDate():
    myFlights = searchByCity(aCity)
    for i in myFlights:
        print(i)

# Fuction Description: Display the flights of a selected city
# Precondition: User inputs a valid city
# Postcondition: List of flights to that city
def searchByCity(aCity):
    openFile()
    flightsofCity=[]
    for i in openFile().values():
        for j in i:
            for y in j:
                if aCity == y:
                    flightsofCity .append(j)
    return flightsofCity
# Fuction Description: Displays the cheapest price of flights
# Precondition: Input of a valid city, and the option to see the cheapest flights
# Postcondition: A list of the cheapest flight per city
def sortByCheapest():
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        myFlights[i][7] = float(myFlights[i][7])
    newFlights=sorted(myFlights, key=lambda i: i[7])
    for i in newFlights:
        print(i)

# Fuction Description: Displays the most expensive price of flights
# Precondition: Input of a valid city, and the option to see the expensive flights
# Postcondition: A list of the expensive flight per city
def sortByExpensive():
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        myFlights[i][7] = float(myFlights[i][7])
    newFlights = sorted(myFlights, key=lambda i: i[7],reverse=True)
    for i in newFlights:
        print(i)

# Fuction Description: Displays the earliest flights of a city
# Precondition: Input of a valid, city and the option to see the earliest flights
# Postcondition: A list of the earliest times of flights
def sortByEarliestTime():
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        conversion=myFlights[i][3].replace(":", "", len(myFlights))
        myFlights[i][3] = conversion
        myFlights[i][3] =int(myFlights[i][3])
    newFlights = sorted(myFlights, key=lambda i: i[3])
    for i in range(len(newFlights)):
        time =str(newFlights[i][3])
        if len(time)==4:
            time=time[:2] + ':' + time[2:]
            newFlights[i][3] = time
        else:
            time = time[:1] + ':' + time[1:]
            newFlights[i][3] = time
    for i in newFlights:
        print(i)
# Fuction Description: Displays the latest flights of a city
# Precondition: Input of a valid, city and the option to see the latest flights
# Postcondition: A list of the latest times of flights
def sortByLatestTime():
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        conversion=myFlights[i][3].replace(":", "", len(myFlights))
        myFlights[i][3] = conversion
        myFlights[i][3] =int(myFlights[i][3])
    newFlights = sorted(myFlights, key=lambda i: i[3],reverse=True)
    for i in range(len(newFlights)):
        time =str(newFlights[i][3])
        if len(time)==4:
            time=time[:2] + ':' + time[2:]
            newFlights[i][3] = time
        else:
            time = time[:1] + ':' + time[1:]
            newFlights[i][3] = time
    for i in newFlights:
        print(i)
# Fuction Description:  Option for user to select a date to see flights
# Precondition: User selects a valid city
# Postcondition: List of the lastest dates of the selected city
def sortByLatestDate():
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        conversion=myFlights[i][4].replace("-", "", len(myFlights))
        myFlights[i][4] = conversion
        myFlights[i][4] =int(myFlights[i][4])
    newFlights = sorted(myFlights, key=lambda i: i[4], reverse=True)
    for i in range(len(newFlights)):
        time =str(newFlights[i][4])
        time=time[:2] + '-' + time[2:4]+"-"+time[4:]
        newFlights[i][4] =time
    for i in newFlights:
        print(i)
#Function descrip: Asks user whether or not they want to pay at the gate
#precondition: must select a flight id
#postcondition will ask user if they are paying with card or at the gate
def payment():
        pay=int(input("How would you like to pay?\n1- Pay online with credit card\n2- Pay at the gate"))
        if pay==1:
            print("Credit Card it is")
            cardNumber=input("Enter your card number: ")
            experiation=input("Enter your experiation date ex. 11/14")
            securityCode=input("Enter the security code found on the back of your card")
            outputFunc()
        else:
            print("Pay at the gate it is...")
            outputFunc()
#Func descript: ouputs the flight information and passenager info to an output file
#precondition: receives nothing, must have flight selected
#postcondition: displays information in output.txt
def outputFunc():
    inputFile = open("output.txt", "w")
    count = 0
    inputFile.write(info)
    inputFile.write("\n"+tickets+" tickets "+ baggage+ " luggages "+ " for "+ totalPrice)
    num=int(tickets)
    for i in range(num):
        count += 1
        print("Please Fill Out the following Information for Passenger #", count)
        inputFile.write("\n***********Confirmation*************\n")
        firstName = input("Enter First Name: ")
        inputFile.write("\n"+"Passanger" + str(count))
        inputFile.write("\n"+firstName+"\n")
        lastName = input("Enter Last Name: ")
        inputFile.write(lastName+"\n")
        phoneNumber= input("Enter a Phone Number: ")
        inputFile.write(phoneNumber+"\n")
        email=input("Enter a email: ")
        inputFile.write(email+"\n")
        age= input("Enter age: ")
        inputFile.write(age + "\n")
        print("Your flight reservation has been confirmed")


# Fuction Description: Function to purchase a ticket
# Precondition: Valid city, time, and price
# Postcondition: Confirmation of a ticket purchase
def purchaseTickets(id):
    global totalPrice
    global info
    global baggage
    global tickets
    myFlights = searchByCity(aCity)
    for i in range(len(myFlights)):
        if myFlights[i][8]==id:
            print("The flight you are purchasing is: ")
            info="\tCity: "+ myFlights[i][0]+" Country: "+myFlights[i][1]+" Continent: "+myFlights[i][2]
            info+="\n\tDeparture Time: "+myFlights[i][3]+" on " +myFlights[i][4]+" Duration: "+myFlights[i][5]+"\n\tAirline Company: " +myFlights[i][6] +" Price per ticket: "+myFlights[i][7]+" ID:"+myFlights[i][8]
            print(info)
            aFlight = myFlights[i]
    conform1=input("Is ths correct (Yes/No)")
    if conform1=="yes":
        tickets=int(input("How many tickets would you like to buy?"))
        price=float(aFlight[7])*tickets
        tickets=str(tickets)
        baggage=int(input("How many bags will you be carrying? 50$ each"))
        bagPrice= 50.00*baggage
        baggage=str(baggage)
        totalPrice= bagPrice+price
        totalPrice=str(totalPrice)
        print("Your total Price is: ",totalPrice)
        payment()
    else:
        print("Exiting purchase window")

# Fuction Description: Checker function to check the cities from the text file
# Precondition: Input of a city
# Postcondition: True and program continues if the city input is true, false otherwise
def isValid(aCity):
    cities=["Paris", "London", "Los Angeles","New York", "Berlin", "Chicago"]
    for i in cities:
        if i==aCity:
            return True
    return False
#Function Description: Displays the first menu for the user
#Precondition: None
#PostCondition: Prints the first menu for the user
def menu1():
    print("Welcome to the Air Flight Search Program!")
    print(
        "Destinations from Austin Bergstorm International Airport: New York, Los Angeles, Chicago, London, Paris, Berlin")
    global aCity
    global flights1
    option1=int(input("Select an option:\n1- Choose a Destination\n2- Exit"))
    while option1!=2:
        if option1==1:
            aCity= input("Enter your Destination")
            aCity = aCity.lower()
            aCity = aCity.capitalize()
            for i in aCity:
                if i == " ":
                    aCity = aCity[:4] + aCity[4].upper() + aCity[5:]
            valid=isValid(aCity)
            if valid==False:
                print("Not a valid destination, try again")
                option1 = int(input("Select an option:\n1- Choose a Destination\n2- Exit"))
            else:
                flights1=searchByCity(aCity)
                menu2()
        elif option1>2 or option1<1:
            print("not a valid option try  again")
            option1 = int(input("Select an option:\n1- Choose a Destination\n2- Exit"))

#Function Description: Displays the second menu for the user
#Precondition: The user must select a destination from the first menu
#PostCondition: Prints the second menu for the user
def menu2():
    option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
    while option2 != 9:
        if option2==1:
            sortByCheapest()
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==2:
            sortByExpensive()
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==3:
            sortByEarliestTime()
            option2 = int(input(
                "Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==4:
            sortByLatestTime()
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==5:
            sortByLatestDate()
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==6:
            earliestDate()
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==7:
            id = input("Enter the Flight ID of the flight you are wanting")
            purchaseTickets(id)
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time  \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
        elif option2==8:
            menu1()
        elif option2>9 or option2<1:
            print("That option is not available! Try again!")
            option2 = int(input("Select an option:\n1- Sort By Cheapest \n2- Sort by Expesive\n3- Sort by Earliest Time \n4-Sort by Latest Time\n5- Sort by Latest Date \n6-Sort by Earliest Date\n7-Purchase a Flight\n8-Choose a different Destination\n9-Exit"))
menu1()