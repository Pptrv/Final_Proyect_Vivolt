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
from config import login_data, client_cups

# Función para descargar el consumo del cliente desde la intranet de Opción Energía
def download_consumo(login_data, client_cups):
    def download_consumo(login_data, client_cups, url):
    driver = webdriver.Chrome("../Programas/chromedriver")
    driver.get(url)
    sleep(1.5)
    driver.find_element_by_name("user").send_keys("vivolt")
    driver.find_element_by_name("password").send_keys("temporal01vivolt")
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/app-root/app-agents/app-layout/app-login/section/div/div/div/div/form/div[2]/div[5]/div/div/div/button").send_keys(Keys.RETURN)
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="main_navbar"]/div[2]/div[1]/div[2]/ul[6]/li').click()
    sleep(0.5)
    driver.find_element_by_name("Cups").send_keys("ES0021000007463134RE")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[1]/button').click()
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[3]/button').click()

# Funcion para importar el consumo del cliente en df
def import_ConsumoCliente():
    list_of_files = glob.glob('/Users/pptrv/Downloads/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    data = pd.read_csv(latest_file, sep=";;", error_bad_lines = False)
    return(data)

# Funcion para guardar el consumo del cliente en 2 df
def saving_ConsumoCliente():
    df_sips = import_ConsumoCliente()
    df_sips_potencia = df_sips.iloc[1:7]
    df_sips_potencia.columns = ['a', 'b'] 
    df_sips_potencia[['Potencia','kWp']] = df_sips_potencia['b'].str.split(";",expand=True)
    df_sips_energia = df_sips.tail(6)
    df_sips_energia.to_csv("../Data/csv/bd_consumo_energia_cliente.csv", index = False)
    df_sips_potencia.to_csv("../Data/csv/bd_consumo_potencia_cliente.csv", index = False)

# Función para llamar a BD_Consumo
def bd_consumo():
    return(bd_consumo_energia_cliente = pd.read_csv("../Data/csv/bd_consumo_energia_cliente.csv"), bd_consumo_potencia_cliente = pd.read_csv("../Data/csv/bd_consumo_potencia_cliente.csv"))
    