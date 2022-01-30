import module1
print("\t\tAirline Reservation System")
print("\t\t\tFlight Details")
print("--------------------------------------------------------------------------------------")
print("| Flights  |  Departure |  Arrival    |      Date          |   Time   |  Total Seats |")
print("--------------------------------------------------------------------------------------")
print("| Flight 1 | Delhi      |   Dubai     |  20th August 2020  |  8:30    |     100      |")
print("| Flight 2 | Fiji       |   Moscow    |  25th August 2020  |  16:30   |     250      |")
print("| Flight 3 | Baghdad    |   Budapest  |  29th August 2020  |  1:00    |     200      |")
print("--------------------------------------------------------------------------------------")
print("\t\t\tPrice Details")
print("-----------------------------")
print("|     Item      |   Price   |")
print("----------------------------|")
print("| Adult Ticket  | 4000  INR |") 
print("| Child Ticket  | 2000  INR |") 
print("| Economy Class | 4000  INR |")
print("| Business Class| 8000  INR |")
print("| First Class   | 15000 INR |")
print("----------------------------")
print("\t\t\tMain Menu")
print("1. Book a Ticket(s)")
print("2. Update Booking Details (class/meal)")
print("3. Display Details of a Passenger")
print("4. Delete Reservation")
print("5. Display Seat Availability")
def main():
    c=int(input("Enter choice from Main Menu: "))
    if c==1:
        mod_func.book()
    elif c==2:
        mod_func.update()
    elif c==3:
        mod_func.display()
    elif c==4:
        mod_func.delbooking()
    elif c==5:
        mod_func.seatavail()
    else:
        print("Invalid Choice")
ans="yes"   
while ans=="yes":
    main()
    ans=input("Do you want to continue? (yes/no): ")
    if ans=="no":
        print("Thank you, Goodbye! ")