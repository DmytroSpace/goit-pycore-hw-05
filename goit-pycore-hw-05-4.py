def input_error(func):                                      # initialition of decorator for different exceptions during using bot
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command arguments."

    return inner

@input_error
def add_contact(contacts, name, phone):                     # extract name and phone number from args and add to dictionary
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(contacts, name, phone):                  # extract name and phone number from args and update dictionary
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."

@input_error
def show_phone(contacts, name):                             # extract name from args and look up phone number in dictionary
    if name in contacts:
        return contacts[name]
    else:
        return None

@input_error
def show_all(contacts):                                     # show all contacts in dictionary
    return contacts

def parse_input(user_input):                      
    cmd, *args = user_input.split()                         # split input into command and arguments
    cmd = cmd.strip().lower()                               # convert to lowercase for case insensitivity
    return cmd, args

def main():
    contacts = {}                                           # create new clean dictionary
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
                                                            # commands block
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) < 2:
                print("Give me name and phone please.")
            else:
                name, phone = args
                print(add_contact(contacts, name, phone))
        elif command == "change":
            if len(args) < 2:
                print("Give me name and phone please.")
            else:
                name, phone = args
                print(change_contact(contacts, name, phone))
        elif command == "phone":
            if len(args) < 1:
                print("Enter the argument for the command")
            else:
                name = args[0]
                result = show_phone(contacts, name)
                if result is not None:
                    print(f'Phone number for contact {name}: {result}')
                else:
                    print('Contact not found.')
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
