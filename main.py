phonebook = {}

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print('No user with this name')
        except ValueError:
            print('Give me name and phone please')
        except IndexError:
            print('Enter user name')
    return inner

@error_handler
def hello(command, name, number):
    print("How can I help you?\n")

@error_handler    
def add(command, name, number):
    if name in phonebook:
        print("This name already exists. Try another!")
    else:
        phonebook[name] = number
        print(f"You added name: {name} and phone number: {number} to your phonebook") 

@error_handler     
def change(command, name, number):
    if name in phonebook:
        phonebook[name] = number
        print(f"You changed your phone number to {number}")
    else:
        raise KeyError

@error_handler 
def phone(command, name, number):
    return phonebook[name]

@error_handler              
def show_all():
    return phonebook

def exit():
    return "Good bye!"

def main():
    while True:
        start = input('').split()
        command = start[0].upper()
        name = start[1] if len(start) > 1 else None
        number = start[2] if len(start) > 2 else None

        if command.startswith('HELLO'):
            hello(command, name, number)

        elif command.startswith("ADD") and number:
            add(command, name, number)

        elif command.startswith("CHANGE"):
            change(command, name, number)

        elif command.startswith("PHONE"):
            print(f'Phone number: {phone(command, name, number)}')

        elif command.startswith("SHOW") and name and name.upper().startswith("ALL"):
            print(f'Phonebook:\n {show_all()}')

        elif command.startswith("GOOD") and name and name.upper().startswith("BYE") or command.startswith("CLOSE") or command.startswith("EXIT"):
            print(exit())
            break   

        else:
            print("No commands in list. Try: add/change/phone/show all/good bye/close/exit")

if __name__ == '__main__':
    main()
