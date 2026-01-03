#Testing new user connection
class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone}"

    @classmethod
    def show_phone_directory(cls):
        if not cls.phone_directory:
            return "No contacts found."
        return "\n".join(contact.show_contact() for contact in cls.phone_directory)

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone
        return f"No contact found for {search_name}"

    @staticmethod
    def validate_phone_number(number):
        return number.isdigit() and len(number) >= 8

def main():
    n_contacts = int(input("How many contacts do you want to add? "))
    for _ in range(n_contacts):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        if Contact.validate_phone_number(phone):
            Contact(name, phone)
        else:
            print("Invalid phone number")
while True:
    print("\n---Phone Directory Menu---\n")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show all Contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            main()

        case "2":
            search_name = input("\nSearch contact by name: ")
            print(Contact.search_contact(search_name))

        case "3":
            print("\nPhone Directory")
            print(Contact.show_phone_directory())

        case "4":
            print("Exiting......")
            break
        case _:
            print("Invalid choice")



