import pandas as pd
import json

class JsonParser:   
    def __init__(self):
        self.data=pd.DataFrame()

    def load_file(self, file_path):
        data = open(file_path, "r")
        data=data.read()
        self.set_data(data)
    
    def data2pd(self, data):
        data=json.loads(data)
        file=data["services"]
        data=pd.DataFrame(file)
        self.set_data(data)

    def get_signal_title(self, data, identifier):
        return data[data["id"]==identifier]["title"].item()

    def set_data(self,data):
        self.data=data
    
    def get_data(self):
        return self.data
