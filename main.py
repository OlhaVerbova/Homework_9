from perser import command_recognizer
from command import bot_operation
import command

stop_words = ["good bye", "close", "exit"]

def main():
    command.command_word = ""
    while command.command_word not in stop_words:
        command.command_word = input("Enter the command: ").lower() # The bot is not sensitive to the case of the entered commands
        temp_run = command_recognizer(command.command_word)
        for i in range(len(temp_run)):            
            bot_operation(temp_run[i])


if __name__ == "__main__":
    main()