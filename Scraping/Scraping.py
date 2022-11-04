## Importé las librerías necesarias

from bs4 import BeautifulSoup as bs
import requests as rqst
import pandas as pd
import numpy as np
import lxml.html as html

## Configuro el link de extracción y seteos de la librería BeautifulSoup

website = 'https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2015'
result = rqst.get(website)
content = result.content
soup = bs(content, "lxml")
print (soup.prettify())

## Configuro la fuente de extracción

inmig = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2015')
soupInmig = bs (inmig.content, "html.parser")

## Selecciono los datos que pertenecen a los nombres de la columna thead.

tableHead = soupInmig.thead
print (tableHead)

## Realizo un for para seleccionar los tr y th y generar una nueva lista con los nombres.
rowHeadersInmig = []

for x in tableHead.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig.append(y.text)

rowHeadersInmig
['Países',
 'Inmigrantes hombres',
 'Inmigrantes mujeres',
 'Inmigrantes',
 '% Inmigrantes',
 'Var.']

## Selecciono los datos que pertenecen al tbody.

tableBody = soupInmig.tbody
print(tableBody)

## Realizo un for para seleccionar los tr y los td y generar una nueva lista con los registros.

tableValuesInmig = []
for x in tableBody.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig.append(td_val)
tableValuesInmig[:5]

## Elimimno las posiciones vacías de cada una de las listas.

for i in range(len(tableValuesInmig)):
  tableValuesInmig[i].pop(5)
print(tableValuesInmig)

## Visualizo la información del dataframe.

dataInmig = pd.DataFrame(tableValuesInmig, columns = rowHeadersInmig)
print(dataInmig) 

## Creo una lista nueva eliminando los + de los nombres de países.

newTable = []
for i in range(len(tableValuesInmig)):
  for h in range(len(rowHeadersInmig)):
    newTable.append(tableValuesInmig[i][h].replace(' [+]', ''))
print(newTable)

## Convierto la nueva lista en numpy.array para darle estructura.

InmigBody = np.array(newTable).reshape(len(tableValuesInmig),len(rowHeadersInmig))
InmigBody[:1]

## Genero el Dataframe.

finalInmig2015 = pd.DataFrame(InmigBody, columns=rowHeadersInmig)
print (finalInmig2015)

## Agrego la sentencia para generar el csv.

finalInmig2015.to_csv('finalInmig2015.csv', encoding='utf-8')


### Proceso de scraping para generar el datasets con datos del año 2019

website19 = 'https://datosmacro.expansion.com/demografia/migracion/inmigracion'
result19 = rqst.get(website19)
content19 = result19.content
soup19 = bs(content19, "lxml")
print (soup19.prettify())