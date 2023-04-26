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
            case "get":
                self.return_count()
                if self.view.show_get() == 1:
                    self.view.show_note(self.model.get_note_id(self.view.show_get_id()))
                else:
                    self.view.show_notes(self.model.get_note_date(self.view.show_get_date()))
            case "get -a":
                self.return_count()
                self.view.show_notes(self.model.get_all_notes())
            case "rem":
                self.return_count()
                choice = self.view.show_remove()
                if choice != 0:
                    self.model.remove_note(choice)
            case "save":
                if self.view.show_save() == "y":
                    self.model.save_data()
            case "help":
                self.view.show_help()
            case "exit":
                self.view.show_exit()

    def return_count(self):
        self.view.set_count_data(self.model.get_count())

    def start(self):
        while True:
            user_choice = self.view.input()
            self.switch(user_choice)
