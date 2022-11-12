print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")

contacts={}
Loop = True
while Loop:
    print("********** MENU **********")
    print("1. add an item ")
    print("2. search ")
    print("3. exit ")
    print("**************************")
    print("")

    Option = int(input("please choose from the menu: "))
    print("")
    if Option == 1:
        Name= str(input("Please enter your name (example: Godfrey C. Vila) : ").capitalize())
        Age= int(input("How old are you: "))
        Address = input("Tell me your address: ").capitalize()
        Phone = int(input("please indicate your phone number: #"))
        contacts = {Name: {"Age": Age, "Address": Address, "Phone": Phone}}
        print("Saved")
        print(contacts)
    elif Option == 3:
        print("Exit")
        Loop = False



