import pandas as pd

# Función calling BD_Precio_Indexado
def bd_precio_indexado():
    return (pd.read_csv("../Data/csv/precios_indexados.csv")

# Función calling BD_Precio_Fijo
def bd_precio_fijo():
    return (pd.read_csv("../Data/csv/precios_fijos.csv")

