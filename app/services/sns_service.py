# Import necessary libraries
import requests
import time
from selenium import webdriver

from app.utils.functions import find_first_element, find_elements_by_regex, find_elements_by_tag, click_element_by_text, find_links_to_excel_files, download_excel_files_from_url

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

# General information services


class GeneralService:
    # Get the about intitution information
    def get_about(url='https://sns.gob.do/sobre-nosotros/quienes-somos/'):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_first_element(response, 'p')
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None

    def get_available_services(url):
        return None

# Stats Service


class StatsService:
    general_url = "https://sns.gob.do/transparencia/estadisticas-institucionales/"

    # Get the title intitution information
    def get_title(url=general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_first_element(response, 'h2')
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None

    # Get the stats years available in the institution
    def get_available_years(url=general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_elements_by_regex(r'\b\d{4}\b', container_tag='div', container_class='wpfd-categories', response=response)
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None

    # Get the stats quaters years available in the institution
    def get_available_quaters(year, url=general_url):
        # Open in headless browser
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        # Click the year
        click_element_by_text(driver, year)

        return find_elements_by_tag(tag="span", content=driver.page_source, container_tag='div', container_class='wpfd-categories', exceptions=['Atrás'])

     # Get the stats quaters years available in the institution
    def get_stats_year(year, url=general_url):
        # Open in headless browser
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        # Click the year
        click_element_by_text(driver, year)

        elements = StatsService.get_available_quaters(year=year)

        for element in elements:
            driver.get(url)
            # Click the year
            click_element_by_text(driver, year)

            # Click the quaters
            click_element_by_text(driver, element)

            content = driver.page_source
            excel_links = find_links_to_excel_files(content)

            # Download the Excel file
            folder_name = f"downloads/sns/{year}"
            download_excel_files_from_url(excel_links, folder_name)

        driver.close()

# Budget Service


class BudgetService:
    general_url = "https://sns.gob.do/transparencia/presupuesto/"

    # Get the title intitution information
    def get_title(url=general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_first_element(response, 'h2')
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None

    # Get the budget items available in the institution
    def get_available_budgets(url=general_url):
        # Make an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            return find_elements_by_tag(tag="span", container_tag='div', container_class='wpfd-categories', response=response,)
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve data. Status code: {response.status_code}")
            return None

    # Get available budget items
    def get_available_budget_items_click(budget, url=general_url):
        # Open in headless browser
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        # Click the year
        click_element_by_text(driver, budget)

        return find_elements_by_tag(tag="span", content=driver.page_source, container_tag='div', container_class='wpfd-categories', exceptions=['Atrás'])

    def get_approved_budget_year(year, url=general_url, name_year=None):
        # Open in headless browser
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        time.sleep(2)

        # Click the year
        click_element_by_text(driver, year)

        content = driver.page_source
        excel_links = find_links_to_excel_files(content)

        # Download the Excel file
        folder_name = f"downloads/sns/{name_year}/budget/approved/"
        download_excel_files_from_url(excel_links, folder_name)

        driver.close()

    def get_executed_budget_year(year, url=general_url, name_year=None):
        # Open in headless browser
        driver = webdriver.Firefox(options=options)
        driver.get(url)

        time.sleep(2)

        # Click the year
        click_element_by_text(driver, year)

        elements = find_elements_by_tag(tag="span", content=driver.page_source,
                                        container_tag='div', container_class='wpfd-categories', exceptions=['Atrás'])

        for element in elements:
            driver.get(url)

            # Click the year
            click_element_by_text(driver, year)

            # Click the month
            click_element_by_text(driver, element)

            content = driver.page_source
            excel_links = find_links_to_excel_files(content)

            # Download the Excel file
            folder_name = f"downloads/sns/{name_year}/budget/executed/{element}"
            download_excel_files_from_url(excel_links, folder_name)

        driver.close()

        # content = driver.page_source
        # excel_links = find_links_to_excel_files(content)

        # # Download the Excel file
        # folder_name = f"downloads/sns/{year}/budget/approved/"
        # download_excel_files_from_url(excel_links, folder_name)

        # driver.close()
