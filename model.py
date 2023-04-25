import json


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
                SAMPLE_DATA = {"count": 0, "notes": [{}]}
                json.dump(SAMPLE_DATA, db)
                self.data = SAMPLE_DATA


    def get_data(self):
        return self.data


model = model()

print(model.get_data())
