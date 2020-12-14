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
    driver.find_element_by_name("Cups").send_keys("ES0021000005204736CV")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[1]/button').click()
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="pcoded"]/div[2]/div/div/div/div/div/div/div/app-sips/div[2]/div/form/div[2]/div/div[3]/button').click()

# Funcion para guardar el consumo del cliente

# Función para llamar a BD_Consumo
def bd_consumo():
    return (pd.read_csv("../Data/csv/consumo_cliente.csv")