import pandas as pd
from copy import deepcopy
import graph_generation as gg

class DataStructure:
    def __init__(self, json_file):
        self.json_file = json_file
        self.df = pd.read_json(json_file)
    
    def decribe_df(self):
        data = deepcopy(self.df)
        return data.describe()
    
    def info_df(self):
        data = deepcopy(self.df)
        return data.info()


if __name__ == "__main__":
    image_base64 = []
    data_structure = DataStructure("Prueva_J.json")
    
    data_structure.describe_df()
