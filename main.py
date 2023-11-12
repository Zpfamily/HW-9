def error_handler(func):
    def inner():
        try:
            result = func()
            return result
        except KeyError:
            print('No user with this name')
        except ValueError:
            print('Give me name and phone please')
        except IndexError:
            print('Enter user name')
    return inner

dict = {}

@error_handler
def hello():
    print("How can I help you?\n")
    
@error_handler    
def add():
    name = start[1]
    value = start[2]
    if start[1] in dict:
        print("This name is exist. Try another!")
    else:
        dict[name] = value
        print(f"You added name: {name} and phonenumber: {value} to your phonebook") 
      
    

@error_handler     
def change():
    
    if start[1] in dict:
        dict[start[1]] = start[2]
        print(f"You change your phonenumber to {start[2]}")
    else:
        raise KeyError
     
    
    
@error_handler 
def phone():
    print(f'Phonenumber: {dict[start[1]]}')
        
@error_handler              
def show_all():
    print(f'Phonebook:\n {dict}')
 
  
def exit():
    print("Good bye!")

    

while True:

    start = input('').split()
   
        
    if start[0].upper().startswith('HELLO'):
        hello()
        
    elif start[0].upper().startswith("ADD"):
        add()
       
    elif start[0].upper().startswith("CHANGE"):
        change()
    
    elif start[0].upper().startswith("PHONE"):
        phone()
        
    elif len(start) > 1 and start[0].upper().startswith("SHOW") and start[1].upper().startswith("ALL"):
        show_all()
     
    elif len(start) > 1 and start[0].upper().startswith("GOOD") and start[1].upper().startswith("BYE") or start[0].upper().startswith("CLOSE") or start[0].upper().startswith("EXIT"):
        exit()
        break   
 
    else:
        print("No commands in list. Try: add/change/phone/show all/good bye/close/exit")
       
    

        
    

  
