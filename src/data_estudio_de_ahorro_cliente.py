# Librerías
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn as sns

# calling BD_Estudio_de_Ahorro
def bd_cliente_estudio_de_ahorro():
    return (bd_cliente_estudio_de_ahorro_modelo = pd.read_csv("../Data/csv/cliente_estudio_de_ahorro_modelo.csv"))