def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return "No such name in contacts."
    
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

def show_all(contacts):
    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result
