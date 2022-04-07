import json
from datetime import datetime


class Writter:
    """
    A class used to write analysis to a json file.

    Writer()

    Attributes
    ----------
            private:
                dict: dict
                    python dict used to write the json file

    Methods
    -------
            public:
                write(analysis: string, data: dict)
                    adds analysis, data to dict key-value pairs
                complete()
                    saves the analysis file
    """
    def __init__(self):
        self.dict = {}

    def write(self, analysis: str, data: dict):
        """
        Adds analysis, data to dict key-value pairs.

                Parameters:
                        analysis (str): Analysis name
                        data (dict): data for the analysis
        """
        self.dict[analysis] = data

    def complete(self):        
        """
        Saves json formatted dict to a txt file.
        """
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        
        json_object = json.dumps(self.dict, indent=2)
        file_name = 'analysis_{}.txt'.format(current_time)

        with open(file_name, 'w') as file:
            file.write(json_object)
