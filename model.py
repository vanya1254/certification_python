import json


class model():
    """отвечает за любое взаимодействие с данными"""

    def __init__(self):
        self.db = json.load("database")
