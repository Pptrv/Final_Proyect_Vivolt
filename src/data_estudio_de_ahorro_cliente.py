# Librerías
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn as sns

# Reading excel as df
def leer_excel_datos_cliente(filename):
    return pd.read_excel("../Data/excel/BD_Clientes_Estudio_de_Ahorro.xlsx", engine='openpyxl')


#save df into csv
def save_datoscliente_df_a_csv():
    return(cliente_estudio_de_ahorro.to_csv("../Data/csv/cliente_estudio_de_ahorro_modelo.csv", index = False))

# Llamar al csv
def bd_cliente_estudio_de_ahorro():
    return (bd_cliente_estudio_de_ahorro_modelo = pd.read_csv("../Data/csv/cliente_estudio_de_ahorro_modelo.csv"))
