# Librerias 

# Calcular la factura de 1 año con los precios actuales del cliente
def importe_factura_año():
    coste_energía_actual = ((bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P1"] * bd_consumo_energia_cliente.iloc[0][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P2"] * bd_consumo_energia_cliente.iloc[1][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P3"] * bd_consumo_energia_cliente.iloc[2][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P4"] * bd_consumo_energia_cliente.iloc[3][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P5"] * bd_consumo_energia_cliente.iloc[4][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Energia_P6"] * bd_consumo_energia_cliente.iloc[5][-1]) )
    coste_potencia_actual =((bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P1"] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P2"] * bd_consumo_potencia_cliente.iloc[1][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P3"] * bd_consumo_potencia_cliente.iloc[2][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P4"] * bd_consumo_potencia_cliente.iloc[3][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P5"] * bd_consumo_potencia_cliente.iloc[4][-1]) +
                        (bd_cliente_estudio_de_ahorro_modelo["Precio_Potencia_P6"] * bd_consumo_potencia_cliente.iloc[5][-1]) ) * 365  
    coste_impuesto_energia = (coste_potencia_actual + coste_energía_actual)* 0.0511
    coste_contador = bd_cliente_estudio_de_ahorro_modelo["Precio_Contador"]*365
    coste_iva = (coste_energía_actual + coste_potencia_actual + coste_impuesto_energia + coste_contador) * 0.21
    actual_coste_anual_cliente = (coste_energía_actual + coste_potencia_actual + coste_impuesto_energia + coste_contador + coste_iva)
    return actual_coste_anual_cliente
    
# Calcular la factura de 1 año con los nuevos precios 
def importe_nuevas_facturas():
    tarifa_df = bd_precios_fijos.loc[bd_precios_fijos["Tarifa"] == bd_cliente_estudio_de_ahorro_modelo["Tarifa"].values[0]]
    precios_vigentes_comercializadora_df = tarifa_df.loc[tarifa_df["Fecha_Finalizacion"] == '0']
    coste_energia_nuevo_comercializadoras = ((precios_vigentes_comercializadora_df['Precio_Energía_P1'] * bd_consumo_energia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P2'] * bd_consumo_energia_cliente.iloc[1][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P3'] * bd_consumo_energia_cliente.iloc[2][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P4'] * bd_consumo_energia_cliente.iloc[3][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P5'] * bd_consumo_energia_cliente.iloc[4][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Energía_P6'] * bd_consumo_energia_cliente.iloc[5][-1])
                      )
    coste_potencia_nuevo_comercializadoras = ((precios_vigentes_comercializadora_df['Precio_Potencia_P1'] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P2'] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P3'] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P4'] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P5'] * bd_consumo_potencia_cliente.iloc[0][-1]) +
                       (precios_vigentes_comercializadora_df['Precio_Potencia_P6'] * bd_consumo_potencia_cliente.iloc[0][-1]) 
                      )* 365
    coste_impuesto_energia_nuevo = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras)* 0.0511
    precios_vigentes_comercializadora_df["precio_contador"] = bd_cliente_estudio_de_ahorro_modelo["Precio_Contador"].values[0]*365
    coste_contador_nuevo = precios_vigentes_comercializadora_df["precio_contador"]
    coste_iva_nuevo = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras + coste_impuesto_energia_nuevo + coste_contador_nuevo) * 0.21
    nuevo_coste_anual_cliente = (coste_energia_nuevo_comercializadoras + coste_potencia_nuevo_comercializadoras + coste_impuesto_energia_nuevo + coste_contador_nuevo + coste_iva_nuevo)
    return nuevo_coste_anual_cliente

# Elegir LA COMERCIALIZADORA
def comercializadora_seleccionada():
    ordenar_comercializadoras = importe_nuevas_facturas().sort_values(ascending=True)
    the_one_price = ordenar_comercializadoras.head(n=1)
    the_one_comercializadora = bd_precios_fijos.loc[bd_precios_fijos.index == the_one_price.index.values[0]]
    return the_one_price, the_one_comercializadora

# Función para sacar el ahorro en euros
def ahorro_euros():
    ahorro =  importe_factura_año() - importe_nuevas_facturas().values[0]
    return ahorro

# Función para sacar el ahorro en porcentaje
def ahorro_porcentaje():
    porcentage_de_ahorro = (ahorro/actual_coste_anual_cliente)*100
    return porcentage_de_ahorro

# Función para crear y guardar un pie_chart con el consumo del cliente.
def pie_chart_consumo():
    lista_consumo_cliente = list(bd_consumo_energia_cliente[bd_consumo_energia_cliente.columns[-1]][0:6])
    labels = ['P1', 'P2', 'P3']
    sizes = [lista_consumo_cliente[0]+lista_consumo_cliente[3],lista_consumo_cliente[1]+lista_consumo_cliente[4], lista_consumo_cliente[2] + lista_consumo_cliente[5] ]

    plt.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('../Data/Imagenes/pie_chart_consumo_cliente.png', bbox_inches='tight')
