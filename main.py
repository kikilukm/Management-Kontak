# Simple Management Contact

import function


# List Of Dictionary

contact_list = [

    {"name": "Kiki Lukman Hakim", 
    "email": "example@gmail.com", 
    "phone": "089123456756" }

]

while True:
    print("MENU")
    print("1.All Contact")
    print("2.Add New Contact")
    print("3.Delete Contact")
    print("4.Search Contact")
    print("0.Exit Menu")
    
   
    menu = input("Select Menu: ")
   

    if menu == "0":
        break
    elif menu == "1":
        function.contact_display(contact_list)
    elif menu == "2":
        contact = function.add_contact()
        contact_list.append(contact)
    elif menu == "3":
        function.delete_contact(contact_list)
    elif menu == "4":
        function.search_contact(contact_list)
    else:
        print("Sorry..Menu Unavailable..")

print("See You...!")