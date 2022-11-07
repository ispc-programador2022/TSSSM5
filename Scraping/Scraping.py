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

inmig2019 = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion')
soupInmig2019 = bs(inmig2019.content, "html.parser")


### Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead2019 = soupInmig2019.thead
print(tableHead2019)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig2019 = []

for x in tableHead2019.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig2019.append(y.text)
rowHeadersInmig2019

### Se seleccionan los datos pertenecientes a los registros con tbody

tableBody2019 = soupInmig2019.tbody
print(tableBody2019)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig2019 = []
for x in tableBody2019.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig2019.append(td_val)
tableValuesInmig2019[:5]


### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig2019)):
  tableValuesInmig2019[i].pop(5)

print(tableValuesInmig2019)

#Visualizamos la información en un dataframe. 
dataInmig2019 = pd.DataFrame(tableValuesInmig2019, columns = rowHeadersInmig2019)
print(dataInmig2019) 

# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable2019 = []
for i in range(len(tableValuesInmig2019)):
  for h in range(len(rowHeadersInmig2019)):
    newTable2019.append(tableValuesInmig2019[i][h].replace(' [+]', ''))

print(newTable2019)

# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody2019 = np.array(newTable2019).reshape(len(tableValuesInmig2019),len(rowHeadersInmig2019))
InmigBody2019[:1]


## GENERACIÓN DEL DATAFRAME
finalInmig2019 = pd.DataFrame(InmigBody2019, columns=rowHeadersInmig2019)
finalInmig2019.head(1)


## Agrego la sentencia para generar el csv 2019
finalInmig2019.to_csv('finalInmig2019.csv', encoding='utf-8')



### Proceso de scraping para generar el datasets con datos del año 2017

inmig2017 = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2017')
soupInmig2017 = bs(inmig2017.content, "html.parser")


### Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead2017 = soupInmig2017.thead
print(tableHead2017)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig2017 = []

for x in tableHead2017.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig2017.append(y.text)
rowHeadersInmig2017

### Se seleccionan los datos pertenecientes a los registros con tbody

tableBody2017 = soupInmig2017.tbody
print(tableBody2017)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig2017 = []
for x in tableBody2017.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig2017.append(td_val)
tableValuesInmig2017[:5]


### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig2017)):
  tableValuesInmig2017[i].pop(5)

print(tableValuesInmig2017)

#Visualizamos la información en un dataframe. 
dataInmig2017 = pd.DataFrame(tableValuesInmig2017, columns = rowHeadersInmig2017)
print(dataInmig2017) 

# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable2017 = []
for i in range(len(tableValuesInmig2017)):
  for h in range(len(rowHeadersInmig2017)):
    newTable2017.append(tableValuesInmig2017[i][h].replace(' [+]', ''))

print(newTable2017)

# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody2017 = np.array(newTable2017).reshape(len(tableValuesInmig2017),len(rowHeadersInmig2017))
InmigBody2017[:1]


## GENERACIÓN DEL DATAFRAME
finalInmig2017 = pd.DataFrame(InmigBody2017, columns=rowHeadersInmig2017)
finalInmig2017.head(1)


## Agrego la sentencia para generar el csv 2019
finalInmig2017.to_csv('finalInmig2017.csv', encoding='utf-8')



### Proceso de scraping para generar el datasets con datos del año 2005

inmig2005 = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2005')
soupInmig2005 = bs(inmig2005.content, "html.parser")


### Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead2005 = soupInmig2005.thead
print(tableHead2005)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig2005 = []

for x in tableHead2005.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig2005.append(y.text)
rowHeadersInmig2005

### Se seleccionan los datos pertenecientes a los registros con tbody

tableBody2005 = soupInmig2005.tbody
print(tableBody2005)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig2005 = []
for x in tableBody2005.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig2005.append(td_val)
tableValuesInmig2005[:5]


### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig2005)):
  tableValuesInmig2005[i].pop(5)

print(tableValuesInmig2005)

#Visualizamos la información en un dataframe. 
dataInmig2005 = pd.DataFrame(tableValuesInmig2005, columns = rowHeadersInmig2005)
print(dataInmig2005) 

# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable2005 = []
for i in range(len(tableValuesInmig2005)):
  for h in range(len(rowHeadersInmig2005)):
    newTable2005.append(tableValuesInmig2005[i][h].replace(' [+]', ''))

print(newTable2005)

# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody2005 = np.array(newTable2005).reshape(len(tableValuesInmig2005),len(rowHeadersInmig2005))
InmigBody2005[:1]


## GENERACIÓN DEL DATAFRAME
finalInmig2005 = pd.DataFrame(InmigBody2005, columns=rowHeadersInmig2005)
finalInmig2005.head(1)


## Agrego la sentencia para generar el csv 2019
finalInmig2005.to_csv('finalInmig2005.csv', encoding='utf-8')