def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)

    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added."


@input_error
def change_phone(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to {new_phone}."
    else:
        raise KeyError(f"Contact {name} not found.")


@input_error
def show_phone(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        raise KeyError(f"Contact {name} not found.")


@input_error
def show_all():
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(name, phone))
        elif command.startswith("change"):
            _, name, new_phone = command.split()
            print(change_phone(name, new_phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(show_phone(name))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
