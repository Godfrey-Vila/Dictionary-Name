print("********** PROGRAMMED BY:*************")
print("********** GODFREY VILA **************")
print("******** SECTION BSCOE 2-2 ***********")
print("******* Sir Danilo Madrigalejos ******")
print("")

contacts = {}
while True:
    print("********** MENU **********")
    print("")
    print("1. add an item ")
    print("2. search ")
    print("3. exit ")
    print("")
    print("**************************")
    print("")

    Option = int(input("please choose from the menu: "))
    print("")
    if Option == 1:
        Name= str(input("Please enter your name (example: Godfrey Vila) : ").upper())
        Age= int(input("How old are you: "))
        Address = input("Tell me your address: ").upper()
        Phone = int(input("please indicate your phone number: #"))
        Symptoms = str(input("Please enter 'yes' if you have Caught otherwise 'no'" ))
        contacts[Name] = {
                    "Name": Name,
                    "Age": Age,
                    "Address": Address,
                    "Phone": Phone,
                    "Symptoms":{"Caught": Symptoms}
                    }
        print(" Your contacts for medical tracing is Saved!!")
    if Option == 2:
        print("")
        Search_Name = str(input("Enter the name you want to search: ").upper())
        if Search_Name in contacts:
            for key, values in contacts[Search_Name].items():
                print(key, values)
        else:
            print("Sorry! The name you have entered is not available.")
    elif Option == 3:
        break
    elif Option > 3:
        print("Must be from 1-3 only")
    elif Option < 1:
        print("Must be from 1-3 only")




