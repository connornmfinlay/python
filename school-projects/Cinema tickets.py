"""
Connor Finlay
Cinema Tickets
"""

categories = [""] * 4
prices = [0.0] * 4
film_name = ""
valid_number = "false"
ticket_number = 0
ticket_type = " "
totalcost = 0.0


categories[0] = "Adult"
categories[1] = "Child"
categories[2] = "Student"
categories[3] = "OAP"

prices[0] = 8.5
prices[1] = 4.9
prices[2] = 5.5
prices[3] = 4

print("What is the name of the film you would like to see?")
film_name = input()

while valid_number == "false":

        print("Please enter the number of tickets required")
        ticket_number = int(input())

        if ticket_number  > 0 and ticket_number <=5:
            valid_number = "true"

        else:
            valid_number = "false"
            print("You can only buy between 1 and 5 tickets")
for counter in range(0,ticket_number):
    print("What ticket type would you like to buy for tickets", counter + 1,"A for Adult, C for Child, S for Student and O for OAP")
    ticket_type = input()

    if ticket_type == "A" or ticket_type == "a":
        totalcost = totalcost + prices[0]
        print("Your ticket type is:", categories[0]," and your price is",prices[0])

    elif ticket_type == "C" or ticket_type == "c":
        totalcost = totalcost + prices[1]
        print("Your ticket type is:", categories[1], "and your price is",prices[1])

    elif ticket_type == "S" or ticket_type == "s":
        totalcost = totalcost + prices[2]
        print("Your ticket type is:", categories[2], "and your price is",prices[2])

    elif ticket_type == "O" or ticket_type =="o":
        totalcost = totalcost + prices[3]
        print("Your ticket type is:", categories[3], "and your price is",prices[3])

print("The total cost is :", (totalcost))
