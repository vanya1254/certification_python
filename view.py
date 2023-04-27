class View():
    """отвечает за взаимодействие с пользователем"""

    def __init__(self):
        self.HELP = ["\t\t***HELP***\n",
                     "Commands:",
                     "\t'add' - add note",
                     "\t'edit' - edit note",
                     "\t'get' - show note(s)\n"
                     "\t    'get -a' - show all",
                     "\t    'get -af' - show all with date filtering",
                     "\t'rem' - remove note",
                     "\t'save' - save changes",
                     "\t'exit' - close program"
                     ]
        self.INPUT_COMMAND = "\nEnter command: "
        self.INPUT_CHOICE = "Enter number: "
        self.INPUT_ID = "\nEnter the id of note: "
        self.INPUT_HEAD = "Enter the head of note: "
        self.INPUT_BODY = "Enter the body of note: "
        self.INPUT_DATE = "\nEnter the date of note(s): "
        self.INPUT_Y_N = "\nY/n? "
        self.END = "\n\n\nThe end of program."
        self.count_data = 0
        self.note = {}

    def set_count_data(self, count):
        self.count_data = count

    def input(self):
        user_cmd = input(self.INPUT_COMMAND).lower()
        return user_cmd

    def show_add(self):
        print()
        head = input(self.INPUT_HEAD)
        body = input(self.INPUT_BODY)
        print("\nNote added successfully")
        print("Do not forget to save!")
        return head, body

    def show_edit(self):
        id_ = self.check_id()
        head = input(self.INPUT_HEAD)
        body = input(self.INPUT_BODY)
        return id_, head, body

    def show_get(self):
        print("\nBy which tag do you want to search?:\n",
              "\t1. ID\n",
              "\t2. Date (ex. dd.mm.yy)",
              )
        choice = self.check_choice()
        return choice

    def show_get_id(self):
        id_ = self.check_id()
        return id_

    def show_get_date(self):
        date = self.check_date()
        return date

    def show_note(self, user_note):
        self.note = user_note
        print()
        for k, v in self.note.items():
            print(f"\t{k}: {v}")

    def show_notes(self, notes):
        if len(notes) == 0:
            print("\n\nNotes not found")
        else:
            for note in notes:
                self.show_note(note)

    def show_filter(self, filter_notes):
        print("\nSorted notes by date:")
        self.show_notes(filter_notes)

    def show_remove(self):
        id_ = self.show_get_id()
        print(f"\nAre you sure you want to delete note with ID: {id_}?")
        answer = input(self.INPUT_Y_N).lower()
        if answer == "y":
            return id_
        else:
            return 0

    def show_save(self):
        print("\nAre you sure you want to save the data?")
        answer = input(self.INPUT_Y_N).lower()
        if answer == "y":
            return "y"
        else:
            return "n"

    def show_help(self):
        print()
        for line in self.HELP:
            print(f"{line}")

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
                    print(f"\nID must be: 0 < {user_id} <= {self.count_data}")
            except Exception:
                print(f"\n{user_id} is not integer number!")

    def check_choice(self):
        choice_condition = True
        while choice_condition:
            user_choice = input(self.INPUT_CHOICE)
            try:
                int(user_choice)
                if 1 <= int(user_choice) <= 2:
                    # choice_condition = False
                    return int(user_choice)
                else:
                    print(f"\nNumber must be: 1 <= {user_choice} <= 2")
            except Exception:
                print(f"\n{user_choice} is not integer number!")

    def check_date(self):
        date_condition = True
        while date_condition:
            user_date = input(self.INPUT_DATE)
            user_date_split = user_date.split(".")
            try:
                dd = int(user_date_split[0])
                mm = int(user_date_split[1])
                yy = int(user_date_split[2])
                return user_date
            except Exception:
                print(f"\nExample: dd.mm.yy\n"
                      f"Your wrong date: {user_date}")

    def show_exit(self):
        print(self.END)
        exit()
