class View():
    """отвечает за взаимодействие с пользователем"""

    def __init__(self):
        self.HELP = ["***HELP***:",
                     "Commands:",
                     "add - add note",
                     "edit - edit note",
                     "show - show note(s)",
                     "rem - remove note",
                     "save - save changes",
                     "exit - close program"
                     ]
        self.INPUT_MESSAGE = "Enter command: "

    def input(self):
        user_cmd = input(self.INPUT_MESSAGE)
        return user_cmd

    def show_add(self):
        head = input("Enter the head of note: ")
        body = input("Enter the body of note: ")
        print("Note added successfully")
        print("Do not forget to save!")
        return head, body

    def