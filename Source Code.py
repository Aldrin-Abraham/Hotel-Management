import random
import datetime
import time
import winsound #For beep sound

# Global List Declaration 
name=[]
phno=[]
add=[]
checkin=[]
checkout=[]
room=[]
price=[]
rc=[]
p=[]
roomno=[]
custid=[]
day=[]
   
# Global Variable Declaration
i=0
   
# Home Function
def Home():      
    print("################### Welcome to Hotel Mariana ###################")
    print("1- Rooms Info\n2- Booking\n3- Room Service(Menu Card)\n4- Payment\n5- Record\n6- Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print(" ")
        Rooms_Info()
    elif ch == 2:
        print(" ")
        Booking()
    elif ch == 3:
        print(" ")
        restaurant()
    elif ch == 4:
        print(" ")
        Payment()
    elif ch == 5:
        print(" ")
        Record()
    elif ch==6:
        print("Exiting...........")
        
# ROOMS INFO 
def Rooms_Info():
    print("         ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    n=int(input("Enter 0 to go back to Main Menu:"))
    if n==0:
        Home()
    else:
        exit()
        
# Booking function 
def Booking():
        # used global keyword to use global variable 'i'
        global i
        print(" BOOKING ROOMS")
        print(" ")
          
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No: "))
            if len(str(p1))==10:
                a = str(input("Address: "))
                # checks if any field is not empty
                if n!="" and p1!="" and a!="":
                    name.append(n)
                    add.append(a)
                    break
                else:
                    print("\tName, Phone no. & Address cannot be empty..!!")
            else:
                winsound.Beep(400,1000)
                time.sleep(3)
                print("Invalid phone number")
                return(Home())
        ciii=input("Check-In: ")
        cii=str(ciii)
        checkin.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)

        cooo=input("Check-Out: ")   
        coo=str(cooo)
        checkout.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
          
        # checks if check-out date falls after check-in date
        if co[1]<ci[1] and co[2]<ci[2]:
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
              
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass
          
        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)

        import mysql.connector as mc
        con=mc.connect(user="root",host="localhost",database="computerproject22_23",password="",charset="utf8")
        cur=con.cursor()
        val="insert into records (Name,Phoneno,Address,CheckIn,CheckOut) values ('{}',{},'{}','{}','{}')".format(n,p1,a,ciii,cooo)
        cur.execute(val)
        con.commit()
        
        print("----SELECT ROOM TYPE----")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print(("\t\tEnter 0 for Room Prices"))
          
        ch=int(input("Enter your choice:"))
          
        # if-conditions to display alloted room type and it's price
        if ch==0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 4500")
            print(" 4. 3-Bed AC - Rs. 5000")
            ch=int(input("Enter your choice:"))
        if ch==1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")  
            price.append(3500)
            print("Price- 3500")
        elif ch==2:
            room.append('Standard AC')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
        elif ch==3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
        elif ch==4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
        else:
            print(" Wrong choice..!!")
   
  
        # randomly generating room no. and customer id for customer
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
          
          
        # checks if alloted room no. & customer id already not alloted
        while rn in roomno or cid in custid:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
              
        rc.append(0)
        p.append(0)
                
        if p1 not in phno:
            phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==1:
                        phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done..!!")
                        name.pop(i)
                        add.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
        print("")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cid)
        roomno.append(rn)
        custid.append(cid)
        i=i+1
        n=int(input("Enter 0 to go back to Main Menu:"))
        if n==0:
            Home()
        else:
            exit()

# Function used in booking
def date(c):  
    if c[2] >= 2022 and c[2] <= 2023:  
        if c[1] != 0 and c[1] <= 12:  
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:  
                if c[2]%4 == 0 and c[0] <= 29:
                    pass  
                elif c[0]<29:
                    pass
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
               
            # if month is odd & less than equal to 7th  month
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
              
            # if month is even & less than equal to 7th month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
              
            # if month is even & greater than equal to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
              
            # if month is odd & greater than equal to 8th  month 
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:  
                pass
              
            else: 
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()
                  
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
              
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Booking()

# RESTAURANT FUNCTION 
def restaurant():
    ph=int(input("Customer Id: "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("####################################################")
            print("                                       Hotel Mariana                                               ")
            print("####################################################")
            print("                                       Menu Card                                                 ")
            print("####################################################")
            print("\n BEVERAGES                                     26 Dal Fry................ 140.00")
            print("----------------------------------      27 Dal Makhani............ 150.00")
            print(" 1  Regular Tea............. 20.00               28 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 25.00")
            print(" 3  Coffee.................. 25.00                ROTI")
            print(" 4  Cold Drink.............. 25.00                ----------------------------------")
            print(" 5  Bread Butter............ 30.00               29 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 30.00               30 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00               31 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toast Sandwich..... 50.00             32 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00               RICE") 
            print("                                                      ----------------------------------")
            print(" SOUPS                                             33 Plain Rice.............. 90.00")
            print("----------------------------------       34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 110.00              35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 110.00               36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 110.00")
            print(" 14 Sweet Corn............. 110.00               SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00              ----------------------------------")
            print("                                                       37 Plain Dosa............. 100.00")
            print(" MAIN COURSE                                     38 Onion Dosa............. 110.00")
            print("----------------------------------        39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00                40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00                41 Rice Idli.............. 130.00")
            print(" 18 Handi Paneer........... 120.00                42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 Chilli Paneer.......... 140.00                  ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00              ----------------------------------")
            print(" 22 Mix Veg................ 140.00                43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00                44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00                45 Pineapple............... 60.00")
            print(" 25 Aloo Matar............. 140.00                46 Butter Scotch........... 60.00")
            print("Note: Please enter the number corresponding to the items in the menu card one at a time to order the selected item")
            print("Press 0 -to end ")
            ch=1
            while(ch!=0):
                ch=int(input("Enter your choice:"))
                  
                # if-elif-conditions to assign item prices listed in menu card 
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=110
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=120
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=140
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=150
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)
              
            # updates restaurant charges and then appends in 'rc' list 
            r=r+rc.pop(n)
            rc.append(r)    
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n=int(input("Enter 0 to go back to Main Menu:"))
    if n==0:
        Home()
    else:
        exit()
       
                   
# PAYMENT FUNCTION             
def Payment():
      
    ph=str(input("Phone Number: "))
    global i
    f=0
      
    for n in range(0,i):
        if ph==phno[n] :
              
            # checks if payment is not already done
             if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("Enter your choice:"))
                print("\n  Amount: ",(price[n]*day[n])+rc[n])
                ch=input("\nDo you want to Pay to Mariana?Y/N")
                if ch in "Yy":
                    print("\n\n --------------------------------")
                    print("           Hotel Mariana")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                    print(" Restaurant Charges: \t",rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)
                      
                    # pops room no. and customer id from list and 
                    # later assigns zero at same position
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)

                    ch=input("\nDo you want to download the bill?Y/N")
                    if ch in "Yy":
                        time.sleep(3)
                        print("Bill of",name[n],"is being downloaded...")
                        time.sleep(3)
                        print("\nYour file will be downloaded as a text file...")
                        time.sleep(3)
                        print("\nPlease wait....")
                        f=open(""+str(name[n])+".txt","w")
                        f.write("--------------------------------")
                        f.write("\n           Hotel Mariana")
                        f.write("\n--------------------------------")
                        f.write("\n              Bill")
                        f.write("\n--------------------------------")
                        f.write("\n Name: "+name[n])
                        f.write("\nPhone No: "+phno[n])
                        f.write("\nAddress: "+add[n])
                        f.write("\nCheck-In: "+checkin[n])
                        f.write("\nCheck-Out: "+checkout[n])
                        f.write("\nRoom Type: "+room[n])
                        f.write("\nRoom Charges: "+str(price[n]*day[n]))
                        f.write("\nRestaurant Charges:"+str(rc[n]))
                        f.write("\n--------------------------------")
                        f.write("\nTotal Amount: "+str((price[n]*day[n])+rc[n]))
                        f.write("\n--------------------------------")
                        f.write("\n          Thank You")
                        f.write("\n          Visit Again :)")
                        f.write("\n--------------------------------\n")
                        f.close()
                        winsound.Beep(400,1000)
                        time.sleep(3)
                        print("File is downloaded")
                    else:
                        print("You do not have an active booking. Please book to print")
             else:
                  for j in range(n+1,i):
                    if ph==phno[j] :
                        if p[j]==0:
                            pass
                          
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n") 
    if f==0:    
        print("Invalid Phone number")
          
    n = int(input("Enter 0 to go back to Main Menu:"))
    if n == 0:
        Home()
    else:
        exit()
  
# RECORD FUNCTION 
def Record():
    print("####################HOTEL RECORD####################\n")
    import mysql.connector as mc
    con=mc.connect(user="root",host="localhost",database="computerproject22_23",password="",charset="utf8")
    cur=con.cursor()
    q="select * from records"
    cur.execute(q)
    r=cur.fetchall()
    from tabulate import tabulate
    head=["Name","Phone No","Address","Check-In","Check-Out"]
    print(tabulate(r,headers=head,tablefmt="grid"))
    n=int(input("Enter 0 to go back to Main Menu:"))
    if n==0:
        Home()
    else:
        exit()
# Driver Code 
Home()

'''
Output

################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:1
 
         ------ HOTEL ROOMS INFO ------

STANDARD NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water.

STANDARD NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water + Window/Split AC.

3-Bed NON-AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1
Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water.

3-Bed AC
---------------------------------------------------------------
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 
1 Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water + Window/Split AC.


Enter 0 to go back to Main Menu:0
################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:2
 
 BOOKING ROOMS
 
Name: Aldrin Abraham
Phone No: 8289869550
Address: TSRA 25,Thoppil Katteth Road,Thiruvankulam
Check-In: 23/12/2022
Check-Out: 2/01/2023
----SELECT ROOM TYPE----
 1. Standard Non-AC
 2. Standard AC
 3. 3-Bed Non-AC
 4. 3-Bed AC
		Enter 0 for Room Prices
Enter your choice:4
Room Type- 3-Bed AC
Price- 5000

			***ROOM BOOKED SUCCESSFULLY***

Room No. -  305
Customer Id -  42
Enter 0 to go back to Main Menu:0
################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:3
 
Customer Id: 42
####################################################
                                       Hotel Mariana                                               
####################################################
                                       Menu Card                                                 
####################################################

 BEVERAGES                                     26 Dal Fry................ 140.00
----------------------------------      27 Dal Makhani............ 150.00
 1  Regular Tea............. 20.00               28 Dal Tadka.............. 150.00
 2  Masala Tea.............. 25.00
 3  Coffee.................. 25.00                ROTI
 4  Cold Drink.............. 25.00                ----------------------------------
 5  Bread Butter............ 30.00               29 Plain Roti.............. 15.00
 6  Bread Jam............... 30.00               30 Butter Roti............. 15.00
 7  Veg. Sandwich........... 50.00               31 Tandoori Roti........... 20.00
 8  Veg. Toast Sandwich..... 50.00             32 Butter Naan............. 20.00
 9  Cheese Toast Sandwich... 70.00
 10 Grilled Sandwich........ 70.00               RICE
                                                      ----------------------------------
 SOUPS                                             33 Plain Rice.............. 90.00
----------------------------------       34 Jeera Rice.............. 90.00
 11 Tomato Soup............ 110.00              35 Veg Pulao.............. 110.00
 12 Hot & Sour............. 110.00               36 Peas Pulao............. 110.00
 13 Veg. Noodle Soup....... 110.00
 14 Sweet Corn............. 110.00               SOUTH INDIAN
 15 Veg. Munchow........... 110.00              ----------------------------------
                                                       37 Plain Dosa............. 100.00
 MAIN COURSE                                     38 Onion Dosa............. 110.00
----------------------------------        39 Masala Dosa............ 130.00
 16 Shahi Paneer........... 110.00                40 Paneer Dosa............ 130.00
 17 Kadai Paneer........... 110.00                41 Rice Idli.............. 130.00
 18 Handi Paneer........... 120.00                42 Sambhar Vada........... 140.00
 19 Palak Paneer........... 120.00
 20 Chilli Paneer.......... 140.00                  ICE CREAM
 21 Matar Mushroom......... 140.00              ----------------------------------
 22 Mix Veg................ 140.00                43 Vanilla................. 60.00
 23 Jeera Aloo............. 140.00                44 Strawberry.............. 60.00
 24 Malai Kofta............ 140.00                45 Pineapple............... 60.00
 25 Aloo Matar............. 140.00                46 Butter Scotch........... 60.00
Note: Please enter the number corresponding to the items in the menu card one at a time to order the selected item
Press 0 -to end 
Enter your choice:1
Enter your choice:3
Enter your choice:4
Enter your choice:9
Enter your choice:13
Enter your choice:15
Enter your choice:18
Enter your choice:28
Enter your choice:29
Enter your choice:30
Enter your choice:33
Enter your choice:39
Enter your choice:41
Enter your choice:43
Enter your choice:46
Enter your choice:0
Total Bill:  1130
Enter 0 to go back to Main Menu:0
################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:4
 
Phone Number: 8289869550
 Payment
 --------------------------------
  MODE OF PAYMENT
  1- Credit/Debit Card
  2- Paytm/PhonePe
  3- Using UPI
  4- Cash
Enter your choice:4

  Amount:  51130

Do you want to Pay to Mariana?Y/Ny


 --------------------------------
           Hotel Mariana
 --------------------------------
              Bill
 --------------------------------
 Name:  Aldrin Abraham 	
 Phone No.:  8289869550 	
 Address:  TSRA 25,Thoppil Katteth Road,Thiruvankulam 	

 Check-In:  23/12/2022 	
 Check-Out:  2/01/2023 	

 Room Type:  3-Bed AC 	
 Room Charges:  50000 	
 Restaurant Charges: 	 1130
 --------------------------------

 Total Amount:  51130 	
 --------------------------------
          Thank You
          Visit Again :)
 --------------------------------


Do you want to download the bill?Y/Ny
Bill of Aldrin Abraham is being downloaded...

Your file will be downloaded as a text file...

Please wait....
File is downloaded
Enter 0 to go back to Main Menu:0
################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:5
 
####################HOTEL RECORD####################

+----------------------+------------+--------------------------------------------+------------+-------------+
| Name                 |   Phone No | Address                                    | Check-In   | Check-Out   |
+======================+============+============================================+============+=============+
| Ankit Tiwari         | 9437526475 | Khushboo Mantir,Lal Singh Street,Banglore  | 23/11/2022 | 30/12/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Arjit Singh          | 9182731212 | Raksha Vihar,Mikha Singh Street,Pune       | 21/07/2022 | 28/07/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Anirudh Ravichandran | 8236139187 | Jaishree,Albackle Road,Rameswaram          | 02/10/2022 | 17/10/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Neeraj Madhav        | 8536593022 | Veer Samaritan,Patel Street,Kochi          | 12/04/2022 | 18/04/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Thaman S             | 7301938912 | House no.13,Prithvi Gardens,Chennai        | 12/02/2023 | 18/02/2023  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Pritam               | 9237234692 | Rose Cottage,Nehru Street,Bengluru         | 05/07/2022 | 18/07/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Neha Kakkar          | 9542342375 | 28,Rosevilla,Kolkata                       | 12/08/2023 | 25/08/2023  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Mithoon              | 8239173912 | Anupam Mithal,Tagore Road,Firozabad        | 03/02/2022 | 12/02/2022  |
+----------------------+------------+--------------------------------------------+------------+-------------+
| Narendra Modi        | 9348293482 | Milka Singh House,Sardar Street,Gujrat     | 21/06/2023 | 01/07/2023  |
+----------------------+------------+--------------------------------------------+------------+-------------+
Enter 0 to go back to Main Menu:0
################### Welcome to Hotel Mariana ###################
1- Rooms Info
2- Booking
3- Room Service(Menu Card)
4- Payment
5- Record
6- Exit
Enter your choice:6
Exiting...........

'''
