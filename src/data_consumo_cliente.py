# Librerías
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd
import glob
import os

import sys
%load_ext autoreload
%autoreload 2
sys.path.append('../configuration')
from config import login_data, client_cups, url

# Función para descargar el consumo del cliente desde la intranet de Opción Energía
def download_consumo():
    driver = webdriver.Chrome("../Programas/chromedriver")
    driver.get(url)
    sleep(1.5)
    driver.find_element_by_name("user").send_keys(login_data["username"])
    driver.find_element_by_name("password").send_keys(login_data["password"])
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/app-root/app-agents/app-layout/app-login/section/div/div/div/div/form/div[2]/div[5]/div/div/div/button").send_keys(Keys.RETURN)
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="main_navbar"]/div[2]/div[1]/div[2]/ul[6]/li').click()
    sleep(0.5)
    driver.find_element_by_name("Cups").send_keys(client_cups["cups"])
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[1]/button').click()
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[3]/button').click()

# Funcion para importar el consumo del cliente en df
def import_ConsumoCliente():
    list_of_files = glob.glob('/Users/pptrv/Downloads/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    general_df = pd.read_csv(latest_file, sep=";;", error_bad_lines = False)
    power_df = general_df.iloc[1:7]
    power_df.columns = ['a', 'b'] 
    power_df[['Potencia','kWp']] = power_df['b'].str.split(";",expand=True)
    energy_df = general_df.tail(6)
    return energy_df, power_df
