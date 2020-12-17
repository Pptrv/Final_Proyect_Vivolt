<img src="Data/Imagenes/VIVOLT logo 2.png" alt="Vivolt Logo" width="150"/>

# Bright Energy for Bright People

Somos una compañía de gestión y asesoramiento energético, representando a nuestros clientes frente a las comercializadoras de luz y gas. El compañero perfecto de los consumidores energéticos, con un objetivo claro y sencillo: que ahorres dinero, tiempo y emisiones.

## Project Description 
Automatización del Estudio de Ahorro Energético de Vivolt. El estudio de ahorro se genera con el "input" de los datos del cliente que obtenemos de la factura de luz que nos envía. Una vez insertados los datos del cliente en nuestro excel interno, podemos ejecutar el programa para que realice un estudio e identifique cual es la comercializadora que mejor encaja en precio con la distribución de consumo del cliente. El "output del proyecto es un informe en pdf que podemos utilizar en VIVOLT para enviar a nuestros clientes por email. 

## Input
Desde la terminal tenemos que ejecutar : 
python3 main.py

Una vez ejecutado el .py nos pide que metamos el archivo excel:
BD_Clientes_Estudio_de_Ahorro

## Output
Se imprime un estudio de ahorro en pdf. 
El archivo sirve para que los potenciales clientes se decidan a firmar con nuestra empresa, mostrando varios resultados como :
- Ahorro %
- Ahorro €
- Emisiones CO2/kg ahorradas
- Información del cliente como datos de contacto,etc. 

# Librerías utilizadas en el proyecto: 
 - Seaborn
 - Numpy
 - Numpy
 - Selenium
 - Matplotlib
 - Docx
 - Time
 - Glob