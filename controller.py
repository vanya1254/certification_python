import model
import view


class Controller():
    """нужен для взаимодействия view и model"""

    def __init__(self):
        self.model = model.Model()
        self.view = view.View()

    def switch(self, command):
        match command:
            case "add":
                self.model.add_note(self.view.show_add())
            case "edit":
                self.return_count()
                self.model.edit_note(self.view.show_edit())

            # case "show":##show
            #
            # case "rem":##remove

            # case "save":##save

            case "exit":
                self.view.show_exit()

            # case "help":##help

    def return_count(self):
        self.view.set_count_data(self.model.get_count())

    def start(self):
        while True:
            user_choice = self.view.input()
            self.switch(user_choice)
