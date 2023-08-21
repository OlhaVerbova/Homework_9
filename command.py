global command_word

telephone_list = {"Olha":"+380996409040"}
#decorator
def input_error(func):
    def inner(list_text):
        parser_list = list_text.split()
        if len(parser_list) == 3:
            try:
                result = func(list_text)
            except IndexError:
                result = "Invalid input format. Give me name and phone please." 
                print(result)     
            return result        
        if len(parser_list) == 2:
            try:
                result = func(list_text)
            except IndexError:
                result = "Invalid input format. Give me phone please."   
                print(result)    
            return result
        if len(parser_list) == 1 and parser_list[0] == "phone":
            try:
                result = func(list_text)
            except IndexError:
                result = "Invalid input format. Give me phone please."   
                print(result)    
            return result
        if len(parser_list) == 1 and parser_list[0] == "change":
            try:
                result = func(list_text)
            except IndexError:
                result = "Invalid input format. Give me phone please."   
                print(result)    
            return result
    return inner

# main functions
def hello():
    return "How can I help you?"

def show_all():
    format_list = "|{:^30s}|{:^20s}|".format("name", "phone") 
    format_list += "\n"
    format_list += "-"*53
    format_list += "\n"
    for name, phone in telephone_list.items():
        format_list += "|{:<30s}|{:^20s}|".format(name, phone)
        format_list += "\n"
    return format_list

def say_good_bye():
    return "Good bye!"

@input_error
def add_new_telephone_contact(text):    
    text_list = text.split()    
    telephone_list.update({text_list[1].title():text_list[2]})
    print(f"The contact {text_list[1].title()} has been successfully added")
    
@input_error
def change_phone_number(text):
    text_list = text.split()
    telephone_list[text_list[1].title()] = text_list[2]
    print(f"Phone {text_list[1].title()} successfully changed to {text_list[2]}")

@input_error
def show_name_contact(text):
    text_list = text.split()
    for key, value in telephone_list.items():
        if value == text_list[1]:
            print(key)
            return key

def bot_operation(text):
    match text:
        case "hello":
            result = hello()
            print(result)
        case "close":
            result = say_good_bye()
            print(result)
        case "good bye":
            result = say_good_bye()
            print(result)
        case "exit":
            result = say_good_bye()
            print(result)
        case "show all":
            result = show_all()
            print(result)
        case "add":
            result = add_new_telephone_contact(command_word)
            
        case "change":
            result = change_phone_number(command_word)
            
        case "phone":
            result = show_name_contact(command_word)
            
    return result