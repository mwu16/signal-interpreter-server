import pandas as pd
import json

class JsonParser:
    def __init__(self):
        self.data=pd.DataFrame()

    def open_file(self, file_path):
        self.data = open(file_path, "r")
        self.data=self.data.read()
        self.data=json.loads(self.data)

    def load_file(self, file):
        file=file["services"]
        self.data=pd.DataFrame(file)
        return self.data

    def get_signal_title(self, identifier):
        return self.data[self.data["id"]==identifier]["title"].item()
