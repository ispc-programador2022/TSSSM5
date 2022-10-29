# TSSSM5 Inicio de proyecto - Generación y Analisis de información mediante WEB SCRAPING
# Análisis de los movimientos migratorios. 

from bs4 import BeautifulSoup as bs
import requests as rqst
import pandas as pd
import numpy as np
import re

# Se configura la fuente. DATOS "2019"

inmig = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion')
soupInmig = bs(inmig.content, "html.parser")

# Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead = soupInmig.thead
print(tableHead)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig = []

for x in tableHead.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig.append(y.text)
rowHeadersInmig

# Se seleccionan los datos pertenecientes a los registros con tbody

tableBody = soupInmig.tbody
print(tableBody)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig = []
for x in tableBody.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig.append(td_val)
tableValuesInmig[:5]

### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig)):
  tableValuesInmig[i].pop(5)

print(tableValuesInmig)

#Visualizamos la información en un dataframe. 
dataInmig = pd.DataFrame(tableValuesInmig, columns = rowHeadersInmig)
print(dataInmig) 


# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable = []
for i in range(len(tableValuesInmig)):
  for h in range(len(rowHeadersInmig)):
    newTable.append(tableValuesInmig[i][h].replace(' [+]', ''))

print(newTable)


# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody = np.array(newTable).reshape(len(tableValuesInmig),len(rowHeadersInmig))
InmigBody[:1]

### Generación del DataFrame
finalyInmig2019 = pd.DataFrame(InmigBody, columns=rowHeadersInmig)

finalyInmig2019.head(1)