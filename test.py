from selenium import webdriver
import pandas as pd

import re

# from app.utils.data import month_names_dict
# from app.utils.functions import click_element_by_text, find_links_to_excel_files, download_excel_files_from_url
from app.services.sns_service import GeneralService, StatsService, BudgetService

# Reading Source files
# url_sources = pd.read_csv('data/sources_list.csv')
# df = pd.read_csv('data/input.csv')
# df = pd.merge(df, url_sources, on='nombre_corto', how='left')

CONF_HEADLESS_BROWSER = True

# print(pd)

# def download_sns():
#     # Open in browser
#     driver = webdriver.Firefox(options=options)
#     driver.get(base_url)
#     # Click the year
#     click_element_by_text(driver, next_needed_year)

#     # Click the month
#     click_element_by_text(driver, next_needed_month_text)

#     # Find the link to the Excel file
#     content = driver.page_source
#     excel_links = find_links_to_excel_files(content)

#     # Download the Excel file
#     download_excel_files_from_url(excel_links, folder_name)
#     driver.close()
#     return excel_links

# print(GeneralService.get_about('https://sns.gob.do/sobre-nosotros/quienes-somos/'))
# print(StatsService.get_available_years('https://sns.gob.do/transparencia/estadisticas-institucionales/'))
# print(StatsService.get_stats_year(year="2022", url='https://sns.gob.do/transparencia/estadisticas-institucionales/'))
# print(BudgetService.get_available_budget_items(
#     budget='Ejecución del Presupuesto', url='https://sns.gob.do/transparencia/presupuesto/'))

# print(BudgetService.get_available_budget_items(
#     budget='Ejecución de Presupuesto 2023', url='https://sns.gob.do/transparencia/presupuesto/#38-1428-wpfd-ejecucion-de-presupuesto-2023'))

# print(BudgetService.get_approved_budget_year(
#     year='Presupuesto Aprobado del Año 2024', url='https://sns.gob.do/transparencia/presupuesto/#38-241-wpfd-presupuesto-aprobado-del-ano', name_year='2024'))

# print(BudgetService.get_executed_budget_year(
#     year='Ejecución de Presupuesto 2024', url='https://sns.gob.do/transparencia/presupuesto/#38-242-wpfd-ejecucion-del-presupuesto', name_year='2024'))

print(BudgetService.get_annual_budget_report(year='2022',
      url='https://sns.gob.do/transparencia/presupuesto/#38-1541-wpfd-informe-fisicio-financiero-anuales'))
# # main function
# if __name__ == "__main__":
#     for i in range(len(df)):
#         print(df['nombre_corto'][i])
#         # common variables
#         base_url = df['portal'][i].strip()
#         domain = re.findall(r'^(https?://[^/]+)', base_url)[0]
#         next_needed_date = df['query_date'][i]
#         next_needed_year, next_needed_month = next_needed_date.split('_')
#         next_needed_month_text = month_names_dict[next_needed_month]
#         folder_name = f"downloads/{next_needed_date}/{df['nombre_corto'][i]}"
#         options = webdriver.FirefoxOptions()
#         if CONF_HEADLESS_BROWSER:
#             options.add_argument('--headless')
#         # calling the download function
#         eval(f"download_{df['nombre_corto'][i].lower()}")()
