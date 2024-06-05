print("\t\t\t\tRDNA BOOKING SPOT")
import datetime
import random
global now
now = datetime.datetime.now()
menu=1
global name
name=input("Enter passenger name:")
global age
age=input("Enter the age:")
global sex
sex=input("Sex - M/F/T:")
f=open("userdetails.txt","w")
f.write("******************USER DETAILS*********************")
f.write("\nName:")
f.write(name)
f.write("\nAge:")
f.write(age)
f.write("\nsex:")
f.write(sex)
f.write("\n*********************END************************")
f.close()
while(menu==1):
    global options
    print("1)MAIN MENU\n2)BOOKING HISTORY\n3)USER DETAILS\n4)EXIT")
    options=int(input("Enter your option"))
    
    def ava():
        print("Available Dates\n")
        print("1)21/07/2022\n")
        d=int(input("select date:"))
        if d==1:
            print("\t\t\t\tAvailable BUS ROUTES:")
            print("1) COIMBATORE TO CHENNAI\n")
            p=int(input("select your options:"))
            new=['[','1',']', ' ', '\t', '[','2',']', ' ', '[','3',']', '\n', '[','4',']', ' ', '\t', '[','5',']', ' ','[', '6',']', '\t', '\n', '[','7',']', '\t','[', '8', ']',' ','[','9',']','\n', '[','10',']', ' ', '\t', '[','11',']', ' ','[', '12',']','\n', '[','13',']', ' ', '\t', '[','14',']', ' ','[', '15',']','\n', '[','16',']', ' ', '\t', '[','17',']', ' ','[', '18',']','\n', '[','19',']', ' ', '\t', '[','20',']', ' ','[', '21',']',]
            new1=['[','1',']', ' ', '\t', '[','2',']', ' ', '[','3',']', '\n', '[','4',']', ' ', '\t', '[','5',']', ' ','[', '6',']', '\t', '\n', '[','7',']', '\t','[', '8', ']',' ','[','9',']','\n', '[','10',']', ' ', '\t', '[','11',']', ' ','[', '12',']','\n', '[','13',']', ' ', '\t', '[','14',']', ' ','[', '15',']','\n', '[','16',']', ' ', '\t', '[','17',']', ' ','[', '18',']','\n', '[','19',']', ' ', '\t', '[','20',']', ' ','[', '21',']',]

            l1="yes"
            l2="yes"

            seatno=[]
            print()
            if p == 1:
                
                print("\t\t\t\tAvailable Buses")
                print("1) Sabari Travels - 21:00pm to 6:30am\nFare:INR 499 \n"
                      "2) INTERCITY      - 22:00pm to 7:40am\nFare:INR 665")
                b=int(input("Select the options:"))
                if b==1:
                        am=0
                        while(l1=="yes"):
                            am+=1
                            print("***************Seates Available***************")
                            print()
                            f=open("sabari.txt","r")
                            r1=f.read()
                            print(r1)
                            f.close()
                            n=int(input("Enter no.of seats to booked"))
                            for i in range(n):
                                s1=input("enter seat numbers to enjoy your journey :")
                                seatno.append(s1)
                                for k in new:
                                    if s1==k:
                                        new.remove(k)
                        
                                        break
                                    else:
                                        pass
            
                    
                            f=open("sabari.txt","w")
                            f.writelines(new)
                            f.close()
                            
                            l1=input("Do you whish to book other seats \n 'yes' or 'no':")
                        print()
                        print("***************INVOICE***************")
                        print()
        
                        f=open("sabari_e_bill.txt","w")
                        f.write("***********Sabari Bus Travels*********\n")
                        f.write("Invoice NO:\t")
                        X=random.randint(0,10000)
                        f.write(str(X))
                        f.write("\nName of the passenger:\t")
                        f.write(name)
                        f.write("\nAge:\t\t\t")
                        f.write(age)
                        f.write("\nSex:\t\t\t")
                        f.write(sex)
                        f.writelines("\nSeat no. booked :\t")
                        
                        f.writelines(seatno)
                        f.write("\nTime Of Booking:\t")
                        f.write(str(now))

                        
                        f.writelines("\nTotal Amount :\t")
                        amount=str(n*499*am)
                        f.write("\tINR ")
                        f.write(amount)
                        f.write("\n****************************************************")
                        f.close()

                        f=open("sabari_e_bill.txt","r")
                        print(f.read())
                        f.close()
                elif b==2:
                        am=0
                        while(l1=="yes"):
                            am+=1
                            print("***************Seates Available***************")
                            print()
                            f=open("intercity.txt","r")
                            r1=f.read()
                            print(r1)
                            f.close()
                            n=int(input("Enter no.of seats to booked"))
                            for i in range(n):
                                s1=input("enter seat numbers to enjoy your journey :")
                                seatno.append(s1)
                                for k in new1:
                                    if s1==k:
                                        new1.remove(k)
                        
                                        break
                                    else:
                                        pass
            
                    
                            f=open("intercity.txt","w")
                            f.writelines(new1)
                            f.close()
                            
                            l1=input("Do you whish to book other seats \n 'yes' or 'no':")
                        print()
                        print("***************INVOICE***************")
                        print()
        
                        f=open("intercity_e_bill.txt","w")
                        f.write("***********Intercity Bus Travels*********\n")
                        f.write("Invoice NO:\t\t")
                        X=random.randint(0,10000)
                        f.write(str(X))
                        f.write("\nName of the passenger:\t")
                        f.write(name)
                        f.write("\nAge:\t\t\t")
                        f.write(age)
                        f.write("\nSex:\t\t\t")
                        f.write(sex)
                        f.writelines("\nSeat no. booked :\t")
                        
                        f.writelines(seatno)
                        f.write("\nTime Of Booking:\t")
                        f.write(str(now))

                        
                        f.writelines("\nTotal Amount :\t\t")
                        amount=str(n*665*am)
                        f.write("INR ")
                        f.write(amount)
                        f.write("\n****************************************************")
                        f.close()

                        f=open("intercity_e_bill.txt","r")
                        print(f.read())
                        f.close()
            else:
                print("invalid option given or options are upcomming")
        else:
            print("Incorrect date provided")

    def history():
        f=open("sabari_e_bill.txt","r")
        print(f.read())
        f.close()
        f=open("intercity_e_bill.txt","r")
        print(f.read())
        f.close()
    def user():
        f=open("userdetails.txt","r")
        print(f.read())
        f.close()
    

    if options==1:
        ava()
    elif options==2:
        history()
        print("1)Previous Page")
        menu=int(input("Choice:"))
    elif options==3:
        user()
        print("1)Previous Page")
        menu=int(input("Choice:"))
    else:
        menu=2
        print("********************************THANKS FOR VISITING********************************")
    

        
