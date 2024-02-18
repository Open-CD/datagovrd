# Import necessary libraries
import requests

from app.utils.functions import find_first_element, find_elements_by_regex

# General information services

class GeneralService:
    # Get the about intitution information 
    def get_about(url = 'https://sns.gob.do/sobre-nosotros/quienes-somos/'):
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
    
    def get_available_services(url):
        return None

class StatsService:
    general_url = "https://sns.gob.do/transparencia/estadisticas-institucionales/"

     # Get the title intitution information 
    def get_title(url = general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_first_element(response, 'h2')
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None
        
    # Get the stats years available in the institution  
    def get_available_years(url = general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_elements_by_regex(response, r'\b\d{4}\b', container_tag='div', container_class='wpfd-categories')
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None
    
