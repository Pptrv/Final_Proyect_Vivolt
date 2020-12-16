import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn as sns
import numpy as np
import datetime as dt

# Funcion convertir excel a csv
def leer_excel_preciosfijos():
    return(precio_fijo_df = pd.read_excel("../Data/excel/BD_Precios_Fijos.xlsx", engine='openpyxl'))

# Cleaning data 
def fecha_inicio_to_datetime():
    precio_fijo_df['Fecha_Inicio'] = pd.to_datetime(precio_fijo_df['Fecha_Inicio'], infer_datetime_format=True)

def fecha_finalizacion_to_datetime():
    precio_fijo_df['Nueva_Fecha_Finalización'] = pd.to_datetime(precio_fijo_df['Fecha_Finalización'], infer_datetime_format=True)
    precio_fijo_df.drop(['Fecha_Finalización'], axis=1, inplace = True)
    precio_fijo_df.rename(columns={'Nueva_Fecha_Finalización': 'Fecha_Finalizacion'}, inplace=True)

def fillna_preciofijo():
    precio_fijo_df.fillna(0, inplace=True)

def change_mwh_to_kwh():
    precio_fijo_df['Precio_Potencia_P1'] = precio_fijo_df['Precio_Potencia_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P2'] = precio_fijo_df['Precio_Potencia_P2'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P3'] = precio_fijo_df['Precio_Potencia_P3'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P4'] = precio_fijo_df['Precio_Potencia_P4'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P5'] = precio_fijo_df['Precio_Potencia_P5'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P6'] = precio_fijo_df['Precio_Potencia_P6'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Potencia_P6'] = precio_fijo_df['Precio_Potencia_P6'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P1'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P2'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P3'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P4'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P5'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)
    precio_fijo_df['Precio_Energía_P6'] = precio_fijo_df['Precio_Energía_P1'].apply(lambda x: x/1000 if x>0.5 else x)

# save df as csv
def save_preciosfijos_csv():
    return(precio_fijo_df.to_csv("../Data/csv/precios_fijos.csv", index = False))

# Función calling BD_Precio_Fijo
def bd_precio_fijo():
    return (pd.read_csv("../Data/csv/precios_fijos.csv")


