#Airline Reservation System
#binary files-flight1.dat,flight2.dat,flight3.dat
import os
import pickle
def book():
    fc=int(input("Enter flight choice: "))#flight choice
    print()
    if fc==1:
        file=open("flight1.dat","ab")
    elif fc==2:
        file=open("flight2.dat","ab")
    elif fc==3:
        file=open("flight3.dat","ab")
    else:
        print("Invalid Option")
        return
    n=int(input("Enter number of passengers: "))
    print()
    for i in range(1,n+1):
        print("Details of Passenger ",i)
        pno=input("Enter passport Number : ")
        name=input("Enter name : ")
        age=int(input("Enter age: "))
        meal=input("Enter meal preference as 'veg' or 'nonveg': ")  #veg/non-veg
        cls=input("Enter class preference as 'economy','business' or 'first': ")  #economy,business,first class
        agec=clsc=0   #agecost and classcost
        if age>12:
            aget="Adult"  #agetype
            agec=4000   #all charges in rupees
        else:
            aget="Child"
            agec=2000
        if cls.lower()=="economy":
            clsc=4000
        elif cls.lower()=="business":
            clsc=8000
        elif cls.lower()=="first":
            clsc=15000
        tax=0.1*(agec+clsc)  #10% tax
        cost=agec+clsc+tax
        print("\nPrice of Ticket for Passenger ",i)
        print(aget," Price +",cls.capitalize(),"Class Price + Tax (10% of cost)=",end=" ")
        print(agec,"+",clsc,"+",tax,"=",cost," Rs\n")
        l=[pno,name,age,meal,cls,cost]
        pickle.dump(l,file)
    file.close()
def update():
    upd_c=input('Select a preference (class/meal): ') #update choice
    if upd_c.lower()=='class':
        update_class()
    elif upd_c.lower()=='meal':
        update_meal()
    else:
        print('Invalid choice')
def update_class():
    x=input("Enter Passport Number: ") #Authentication
    fc=int(input("Select flight choice (1/2/3): ")) #flight choice
    print()
    try:
        if fc==1:
            f1=open("flight1.dat","rb")
        elif fc==2:
            f1=open("flight2.dat","rb")
        elif fc==3:
            f1=open("flight3.dat","rb")
        elif f1 not in [1,2,3]:
            print("Invalid Option")
            return
    except FileNotFoundError: 
        print("No bookings have been made for this flight")
    updcls=input("Select class preference for updation (first,business,economy): ")  #class to update
    print()
    cls=["first","business","first",]
    clsc=[15000,8000,4000]
    f2=open("temp.dat","wb")
    ctr=0
    try:
        while True: #l=[pno,name,age,meal,cls,cost]
            obj=pickle.load(f1)
            if obj[0]==x:
                if obj[2]>12:
                    agec=4000
                    aget="Adult"
                else:
                    agec=2000
                    aget="Child"
                tax=0.1*(agec+clsc[cls.index(updcls)])
                cost=agec+clsc[cls.index(updcls)]+tax
                pickle.dump(obj[0:4]+[updcls,cost],f2)
                print("Updated Cost: ",aget," Price +",updcls.capitalize(),"Class Price + Tax (10% of cost)=",end=" ")
                print(agec,"+",clsc[cls.index(updcls)],"+",tax,"=",cost," Rs\n")
                print('Class preference has successfully been changed.')
            else:
                pickle.dump(obj,f2)
            ctr=ctr+1
    except EOFError:
        f1.close()
        f2.close()
    if fc==1:
        os.remove("flight1.dat")
        os.rename("temp.dat","flight1.dat")
    elif fc==2:
        os.remove("flight2.dat")
        os.rename("temp.dat","flight2.dat")
    elif fc==3:
        os.remove("flight3.dat")
        os.rename("temp.dat","flight3.dat")
    if ctr==0:
        print("No such booking found")
def update_meal():
    x=input("Enter Passport Number: ") #Authentication
    fc=int(input("Select flight choice (1/2/3): ")) #flight choice
    print()
    try:
        if fc==1:
            f1=open("flight1.dat","rb")
        elif fc==2:
            f1=open("flight2.dat","rb")
        elif fc==3:
            f1=open("flight3.dat","rb")
        elif f1 not in [1,2,3]:
            print("Invalid Option")
            return
    except FileNotFoundError: 
        print("No bookings have been made for this flight")
    updmeal=input("Select meal preference for updation (veg or nonveg): ")  #meal to update
    print()
    f2=open("temp.dat","wb")
    ctr=0
    try:
        while True: #l=[pno,name,age,meal,cls,cost]
            obj=pickle.load(f1)
            if obj[0]==x:
                pickle.dump(obj[0:3]+[updmeal,]+obj[4:6],f2)
                print('Meal preference has successfully been changed.')
            else:
                pickle.dump(obj,f2)
            ctr=ctr+1
    except EOFError:
        f1.close()
        f2.close()
    if fc==1:
        os.remove("flight1.dat")
        os.rename("temp.dat","flight1.dat")
    elif fc==2:
        os.remove("flight2.dat")
        os.rename("temp.dat","flight2.dat")
    elif fc==3:
        os.remove("flight3.dat")
        os.rename("temp.dat","flight3.dat")
    if ctr==0:
        print("No such booking found")
def display():
    x=input("Enter Passport Number: ")  #Authentication
    fc=int(input("Enter flight choice (1/2/3): ")) #flight choice
    ctr=0
    print()
    try:
        if fc==1:
            file=open("flight1.dat","rb")
        elif fc==2:
            file=open("flight2.dat","rb")
        elif fc==3:
            file=open("flight3.dat","rb")
        elif file not in [1,2,3]:
            print("Invalid Option")
            return
    except FileNotFoundError: 
        print("No bookings have been made for this flight")
    try:
        while True:
            obj=pickle.load(file)
            ctr=ctr+1
            if obj[0]==x:
                print('Passport number: ', obj[0])
                print('Name: ', obj[1])
                print('Age: ', obj[2])
                print('Meal: ', obj[3])
                print('Class: ', obj[4])
                print('Cost: ', obj[5])               
    except EOFError:
        file.close()
    if ctr==0:
        print("No bookings have been made for this flight")
def delbooking():
    x=input("Enter Passport Number: ")
    fc=int(input("Enter flight choice: "))#flight choice
    print()
    try:
        if fc==1:
            f1=open("flight1.dat","rb")
        elif fc==2:
            f1=open("flight2.dat","rb")
        elif fc==3:
            f1=open("flight3.dat","rb")
        elif fc not in [1,2,3]:
            print("Invalid Option")
            return
    except FileNotFoundError: #only if file not exists required only when program is run first time
        print("No bookings have been made for this flight") 
    f2=open("temp.dat","wb")
    ctr=0
    try:
        while True:
            obj=pickle.load(f1)
            if obj[0]==x:
                ctr=ctr+1
                pass
            else:
                pickle.dump(obj,f2)
    except EOFError:
        f1.close()
        f2.close()
    if fc==1:
        os.remove("flight1.dat")
        os.rename("temp.dat","flight1.dat")
    elif fc==2:
        os.remove("flight2.dat")
        os.rename("temp.dat","flight2.dat")
    elif fc==3:
        os.remove("flight3.dat")
        os.rename("temp.dat","flight3.dat")
    if ctr==0:
        print("No such record found")
    else:
        print("Booking Cancelled")
def seatavail():
    fc=int(input("Enter flight choice: "))#flight choice
    print()
    try:
        if fc==1:
            f=open("flight1.dat","rb")
            total=100
        elif fc==2:
            f=open("flight2.dat","rb")
            total=250
        elif fc==3:
            f=open("flight3.dat","rb")
            total=200
        elif fc not in [1,2,3]:
            print("Invalid Option ")
            return
    except FileNotFoundError:#only if file not exists, required only when program is run first time
        print("All seats are available")
    ctr=0
    try:
        while True:
            obj=pickle.load(f)
            ctr=ctr+1
    except EOFError:
        f.close()
    print("Number of Seats Available: ",total-ctr)
