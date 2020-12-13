from flask import Flask, request
import markdown.extensions.fenced_code

app = Flask (__name__)

@app.route("/")
def index():
    readme_api = open("README_API.md", "r") 
    md_template_string = markdown.markdown(readme_api.read().extensions = ["fenced_code"])
    return md_template_string

@app.route("/parametros")
def parametros():
    diccionario = { 
    'Titular_de_la_Cuenta' : , 'CIF_/_NIF' : , 'Persona_de_Contacto' : , 'Email' :,
    'Telefono' : , 'Cups' : , 'Dirección_completa' : , 'Tipo_de_cliente' : ,
    'Subtipo_de_cliente' : , 'Mercado_regulado' :, 'Bono_social' : ,
    'Fecha_inicio_del_contrato' : , 'Fecha_final_del_contrato' : ,
    '#_contrato_suministro' : , 'Permanencia' : ,
    'Periodo_facturado_(factura_enviada)' : , 'Comercializadora' : , 'Tarifa' : ,
    'Precio_Energia_P1' : , 'Precio_Energia_P2' : , 'Precio_Energia_P3' : ,
    'Precio_Energia_P4' : , 'Precio_Energia_P5' : , 'Precio_Energia_P6' : ,
    'Precio_Potencia_P1' : , 'Precio_Potencia_P2' : , 'Precio_Potencia_P3' : ,
    'Precio_Potencia_P4' : , 'Precio_Potencia_P5' : , 'Precio_Potencia_P6' : ,
    'Precio_Contador' : , 'Precio_Otros _Servicios_€/mes' : 
    }
    return diccionario

app.run(debug=True)