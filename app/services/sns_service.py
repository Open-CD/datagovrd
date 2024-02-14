# Import necessary libraries
import requests

from utils.functions import find_first_element

# General information services

# Get the about intitution information 
def get_about(url):
     # Make an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
       return find_first_element(response, 'p')
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")
        return None
    
