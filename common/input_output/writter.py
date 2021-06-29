import json
from datetime import datetime


class Writter:
    def __init__(self):
        self.dict = {}

    def write(self, analysis, data):
        self.dict[analysis] = data

    def complete(self):
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        
        json_object = json.dumps(self.dict, indent=2)
        file_name = 'analysis_{}.txt'.format(current_time)

        with open(file_name, 'w') as file:
            file.write(json_object)
