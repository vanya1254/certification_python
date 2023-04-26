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
        self.INPUT_COMMAND = "Enter command: "
        self.INPUT_ID = "Enter the id of note: "
        self.INPUT_HEAD = "Enter the head of note: "
        self.INPUT_BODY = "Enter the body of note: "
        self.count_data = 0

    def set_count_data(self, count):
        self.count_data = count

    def input(self):
        user_cmd = input(self.INPUT_COMMAND)
        return user_cmd

    def show_add(self):
        head = input(self.INPUT_HEAD)
        body = input(self.INPUT_BODY)
        print("Note added successfully")
        print("Do not forget to save!")
        return head, body

    def show_edit(self):
        id_ = self.check_id()
        head = input(self.INPUT_HEAD)
        body = input(self.INPUT_BODY)
        return id_, head, body

    def check_id(self):
        count_condition = True
        while count_condition:
            user_id = input(self.INPUT_ID)
            try:
                int(user_id)
                if self.count_data >= int(user_id) & int(user_id) > 0:
                    # count_condition = False
                    return int(user_id)
                else:
                    print(f"Id must be: 0 < {user_id} <= {self.count_data}")
            except Exception:
                print(f"{user_id} is not integer number!")

    def show_exit(self):
        print("The end of program")
        exit()