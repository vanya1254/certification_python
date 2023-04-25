import model
import view


class Controller():
    """нужен для взаимодействия view и model"""
    def __init__(self):
        self.model = model()
        self.view = view


    def handler(self, command):
        match command:
            case "add":##add

            case "edit":##edit

            case "show":##show

            case "rem":##remove

            case "save":##save

            case "exit":##exit

            case "help":##help

    def start(self):
        while True:
            user_choice = view.input()
            handler(user_choice)