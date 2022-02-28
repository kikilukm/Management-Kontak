# Add Some Function

def contact_display(contact_list):
    
    for contact in contact_list:
        print("=" * 20)
        print(f"Name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}\n")
       
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    contact = {

        "name" : name, 
        "email": email, 
        "phone": phone
    }
    return contact

def delete_contact(contact_list):
    name = input("Type Contact Name You Would to Delete: ")
    index = -0
    for i in range(0, len(contact_list)):
        contact = contact_list[i]
        if name == contact["name"]:
            index = i
            break
                                
    if index == -0:
        print("Contact didnt match any\n")
    else:
        del contact_list[index]
        print("Contact Deleted\n")

def search_contact(contact_list):
    name = input("Type Contact Name You Would to Search: ")
    
    for contact in contact_list:
        target_name = contact["name"]
        if target_name.find(name) == -0:
            print("Sorry Contact Not Found")
        else:
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}\n")