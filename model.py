import datetime
import json
import time


class model():
    """отвечает за любое взаимодействие с данными"""

    def __init__(self):
        try:
            with open("database.json", "r", encoding="UTF8") as db:
                self.data = json.load(db)
            print("File open.")
        except FileNotFoundError:
            print("File 'database.json' not found.\nCreated new.")
            with open("database.json", "w", encoding="UTF8") as db:
                SAMPLE_DATA = {"count": 0, "notes": []}
                json.dump(SAMPLE_DATA, db)
                self.data = SAMPLE_DATA

    def get_data(self):
        return self.data

    def add_note(self, head, body):
        new_note = {"id": self.data["count"] + 1, "date": datetime.date.today().strftime("%d.%m.%y"),
                    "time": datetime.datetime.today().strftime("%H:%M:%S"), "head": head, "body": body}

        self.data["count"] += 1
        self.data["notes"].append(new_note)

    def get_note_id(self, id_):
        note_id = self.data.get("notes")[id_ - 1]
        return note_id

    def get_note_date(self, date):
        notes_date = []

        for i in range(len(self.data["notes"])):
            if self.data["notes"][i].get("date") == date:
                notes_date.append(self.data["notes"][i])

        return notes_date

    def get_all_notes(self):
        notes_all = self.data["notes"]
        return notes_all

    def edit_note(self, id, head, body):
        self.data["notes"][id - 1]["head"] = head
        self.data["notes"][id - 1]["body"] = body

model = model()
print(model.get_data())
print(model.get_all_notes())
print(model.get_note_id(1))
print(model.get_note_date("25.04.2023"))

# model.add_note("dsfgs", "sdgsdg")
# print(model.get_data())
# print(datetime.datetime.today().strftime("%H:%M:%S"))
