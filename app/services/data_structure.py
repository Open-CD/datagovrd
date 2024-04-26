# Import the pandas library to work with tabular data
import pandas as pd
# Import the deepcopy function from the copy library to create a deep copy of an object
from copy import deepcopy

# Definition of the DataStructure class
class DataStructure:
    def __init__(self, json_file):
        # Initialize the DataStructure object with a JSON file
        self.json_file = json_file
        # Read the JSON file and convert it into a pandas DataFrame
        self.df = pd.read_json(json_file)
    
    def decribe_df(self):
        # Create a deep copy of the DataFrame
        data = deepcopy(self.df)
        # Return a statistical summary of the DataFrame
        return data.describe()
    
    def info_df(self):
        # Create a deep copy of the DataFrame
        data = deepcopy(self.df)
        # Return information about the DataFrame, such as column data types and the number of non-null values
        return data.info()

# Main execution block of the program
if __name__ == "__main__":
    # Create an instance of the DataStructure class with the "Prueva_J.json" JSON file
    data_structure = DataStructure("Prueva_J.json")
    # Call the decribe_df() method to get a statistical summary of the DataFrame and save it to a JSON file named "name.json"
    data_structure.decribe_df().to_json("name")
