print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")

Loop = True
while Loop:
    print("********** MENU **********")
    print("1. add an item ")
    print("2. search ")
    print("3. exit ")
    print("**************************")
    Option = int(input("please choose from the menu: "))
    if Option == 1:
        First_Name = str(input("please state your fist name: ").upper())
        Middle_Initial = str(input("please state your middle initial: ").upper())
        Last_Name = str(input("please state your last name: ").upper())
        Age= int(input("How old are you: "))
        Address = input("Tell me your address: ")
        Phone = int(input("please indicate your phone number: #"))
        print("Name: ", First_Name, Middle_Initial, Last_Name)
        print("Age: ", Age)
        print("Address: ", Address)
        print("Phone number: ", Phone)

    Loop = False



