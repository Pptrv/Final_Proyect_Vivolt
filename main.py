# IMPORTS

# Python imports
import sys
import os
import datetime as dt

# Third-party imports
import docx
from docx.shared import Cm
import glob
import numpy as np
import pandas as pd
from pandas import ExcelWriter, ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from docx2pdf import convert

# Project imports
from configuration.config import login_data, client_cups, url
from src.docword import generate_doc

# Other
sys.path.append('configuration')

# CONSTANTS
BD_CLIENT_DATA = input("Nombre del archivo para realizar el estudio de ahorro: " )
BD_CLIENT_DATA_PATH = "Data/excel/" + BD_CLIENT_DATA + ".xlsx"
BD_FIXED_PRICES_PATH = "Data/excel/BD_Precios_Fijos.xlsx"


# CLIENT DATA DF
def get_client_data_df():
    return pd.read_excel(BD_CLIENT_DATA_PATH, engine='openpyxl')

def get_client_data_points(df):
    data_points = {}
    data_points["titular_de_la_cuenta"] = df["Titular_de_la_Cuenta"]
    data_points["direccion_suministro"] = df["Dirección_completa"]
    data_points["cups"] = df["Cups"]
    data_points["records"] = [df["Precio_Energia_P1"], df["Precio_Energia_P2"], df["Precio_Energia_P3"]] # precio energia cliente
    data_points["records_2"] = [df["Precio_Potencia_P1"], df["Precio_Potencia_P2"], df["Precio_Potencia_P3"]] # precio potencia cliente
    return data_points


# FIXED PRICES DF
def fecha_inicio_to_datetime(df):
    df['Fecha_Inicio'] = pd.to_datetime(df['Fecha_Inicio'], infer_datetime_format=True)
    return df

def fecha_finalizacion_to_datetime(df):
    df['Nueva_Fecha_Finalización'] = pd.to_datetime(df['Fecha_Finalización'], infer_datetime_format=True)
    df.drop(['Fecha_Finalización'], axis=1, inplace = True)
    df.rename(columns={'Nueva_Fecha_Finalización': 'Fecha_Finalizacion'}, inplace=True)
    return df

def fillna_preciofijo(df):
    df.fillna(0, inplace=True)
    return df

def change_mwh_to_kwh(df):
    df['Precio_Potencia_P1'] = df['Precio_Potencia_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P2'] = df['Precio_Potencia_P2'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P3'] = df['Precio_Potencia_P3'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P4'] = df['Precio_Potencia_P4'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P5'] = df['Precio_Potencia_P5'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P6'] = df['Precio_Potencia_P6'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Potencia_P6'] = df['Precio_Potencia_P6'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P1'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P2'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P3'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P4'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P5'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    df['Precio_Energía_P6'] = df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    return df

def get_fixed_prices_df():
    df = pd.read_excel(BD_FIXED_PRICES_PATH, engine='openpyxl')
    df = fecha_inicio_to_datetime(df)
    df = fecha_finalizacion_to_datetime(df)
    df = fillna_preciofijo(df)
    df = change_mwh_to_kwh(df)
    return df


# CLIENT CONSUMPTION DFS
def download_consumo():
    driver = webdriver.Chrome("Programas/chromedriver")
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
    client_general_df = pd.read_csv(latest_file, sep=";;", error_bad_lines = False)
    client_power_df = client_general_df.iloc[1:7]
    client_power_df.columns = ['a', 'b'] 
    client_power_df[['Potencia','kWp']] = client_power_df['b'].str.split(";",expand=True)
    client_energy_df = client_general_df.tail(6)
    return client_energy_df, client_power_df

def get_client_consumption_dfs():
    download_consumo()
    client_energy_df, client_power_df = import_ConsumoCliente()
    return client_energy_df, client_power_df


# ESTUDIO DE AHORRO
# Calcular la factura de 1 año con los precios actuales del cliente
def importe_factura_año(client_data_df, client_energy_df, client_power_df):
    coste_energía_actual = ((client_data_df["Precio_Energia_P1"] * float(client_energy_df.iloc[0][-1])) +
                        (client_data_df["Precio_Energia_P2"] * float(client_energy_df.iloc[1][-1])) +
                        (client_data_df["Precio_Energia_P3"] * float(client_energy_df.iloc[2][-1])) +
                        (client_data_df["Precio_Energia_P4"] * float(client_energy_df.iloc[3][-1])) +
                        (client_data_df["Precio_Energia_P5"] * float(client_energy_df.iloc[4][-1])) +
                        (client_data_df["Precio_Energia_P6"] * float(client_energy_df.iloc[5][-1])) )
    coste_potencia_actual =((client_data_df["Precio_Potencia_P1"] * float(client_power_df.iloc[0][-1])) +
                        (client_data_df["Precio_Potencia_P2"] * float(client_power_df.iloc[1][-1])) +
                        (client_data_df["Precio_Potencia_P3"] * float(client_power_df.iloc[2][-1])) +
                        (client_data_df["Precio_Potencia_P4"] * float(client_power_df.iloc[3][-1])) +
                        (client_data_df["Precio_Potencia_P5"] * float(client_power_df.iloc[4][-1])) +
                        (client_data_df["Precio_Potencia_P6"] * float(client_power_df.iloc[5][-1])) ) * 365
    coste_impuesto_energia = (coste_potencia_actual + coste_energía_actual)* 0.0511
    coste_contador = client_data_df["Precio_Contador"]*365
    coste_iva = (coste_energía_actual + coste_potencia_actual + coste_impuesto_energia + coste_contador) * 0.21
    actual_coste_anual_cliente = (coste_energía_actual + coste_potencia_actual + coste_impuesto_energia + coste_contador + coste_iva)
    return actual_coste_anual_cliente.values[0]
    
# Calcular la factura de 1 año con los nuevos precios 
def importe_nuevas_facturas(client_data_df, fixed_prices_df, client_energy_df, client_power_df):
    tarifa_df = fixed_prices_df.loc[fixed_prices_df["Tarifa"] == client_data_df["Tarifa"].values[0]]
    precios_vigentes_comercializadora_df = tarifa_df.loc[tarifa_df["Fecha_Finalizacion"] == 0]
 
    coste_energia_nuevo_comercializadoras = ((precios_vigentes_comercializadora_df['Precio_Energía_P1'] * float(client_energy_df.iloc[0][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P2'] * float(client_energy_df.iloc[1][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P3'] * float(client_energy_df.iloc[2][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P4'] * float(client_energy_df.iloc[3][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P5'] * float(client_energy_df.iloc[4][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P6'] * float(client_energy_df.iloc[5][-1]))
                      )

    coste_potencia_nuevo_comercializadoras = ((precios_vigentes_comercializadora_df['Precio_Potencia_P1'] * float(client_power_df.iloc[0][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P2'] * float(client_power_df.iloc[1][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P3'] * float(client_power_df.iloc[2][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P4'] * float(client_power_df.iloc[3][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P5'] * float(client_power_df.iloc[4][-1])) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P6'] * float(client_power_df.iloc[5][-1])) 
                      )* 365
    coste_impuesto_energia_nuevo = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras)* 0.0511
    precios_vigentes_comercializadora_df["precio_contador"] = client_data_df["Precio_Contador"].values[0]*365
    coste_contador_nuevo = precios_vigentes_comercializadora_df["precio_contador"]
    coste_iva_nuevo = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras + coste_impuesto_energia_nuevo + coste_contador_nuevo) * 0.21
    nuevo_coste_anual_cliente = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras + coste_impuesto_energia_nuevo + coste_contador_nuevo + coste_iva_nuevo)

    ordenar_comercializadoras = nuevo_coste_anual_cliente.sort_values(ascending=True)
    the_one_price = ordenar_comercializadoras.head(n=1)
    the_one_comercializadora = fixed_prices_df.loc[fixed_prices_df.index == the_one_price.index.values[0]]
    return the_one_price, the_one_comercializadora

# Función para crear y guardar un pie_chart con el consumo del cliente.
def pie_chart_consumo():
    consumo_p1_cliente = list(bd_consumo_energia_cliente[bd_consumo_energia_cliente.columns[-1]][0:3])
    labels = ['P1', 'P2', 'P3']
    sizes = [consumo_p1_cliente[0],consumo_p1_cliente[1], consumo_p1_cliente[2] ]
    plt.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('Data/Imagenes/pie_chart_consumo_cliente.png', bbox_inches='tight')

def get_saving_data_points(client_data_df, fixed_prices_df, client_energy_df, client_power_df):
    
    actual_coste_anual_cliente = importe_factura_año(client_data_df, client_energy_df, client_power_df)
    the_one_price, the_one_comercializadora = importe_nuevas_facturas(client_data_df, fixed_prices_df, client_energy_df, client_power_df)
    ahorro = actual_coste_anual_cliente - the_one_price.values[0]

    ahorro_porcentaje = (ahorro/actual_coste_anual_cliente)*100

    return {
        "actual_coste_anual_cliente": actual_coste_anual_cliente,
        "the_one_price": the_one_price,
        "the_one_comercializadora": the_one_comercializadora,
        "ahorro": ahorro,
        "ahorro_porcentaje": ahorro_porcentaje,
    }


# GET DOC DATA
def get_doc_data(client_data_df, fixed_prices_df, client_energy_df, client_power_df):
    doc_data = {}
    doc_data.update(get_client_data_points(client_data_df))
    doc_data.update(get_saving_data_points(client_data_df, fixed_prices_df, client_energy_df, client_power_df))
    return doc_data




# MAIN
def main():
    # GET DFS
    client_data_df = get_client_data_df()
    fixed_prices_df = get_fixed_prices_df()
    client_energy_df, client_power_df = get_client_consumption_dfs()
    
    # ESTUDIO AHORRO
    doc_data = get_doc_data(client_data_df, fixed_prices_df, client_energy_df, client_power_df)

    # GENERATE DOC
    generate_doc(doc_data)

main()