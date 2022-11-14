## Importé las librerías necesarias

from bs4 import BeautifulSoup as bs
import requests as rqst
import pandas as pd
import numpy as np
import lxml.html as html


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


### Proceso de scraping para generar el datasets con datos del año 2000

inmig2000 = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2000')
soupInmig2000 = bs(inmig2000.content, "html.parser")


### Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead2000 = soupInmig2000.thead
print(tableHead2000)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig2000 = []

for x in tableHead2000.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig2000.append(y.text)
rowHeadersInmig2000

### Se seleccionan los datos pertenecientes a los registros con tbody

tableBody2000 = soupInmig2000.tbody
print(tableBody2000)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig2000 = []
for x in tableBody2000.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig2000.append(td_val)
tableValuesInmig2000[:5]


### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig2000)):
  tableValuesInmig2000[i].pop(5)

print(tableValuesInmig2000)

#Visualizamos la información en un dataframe. 
dataInmig2000 = pd.DataFrame(tableValuesInmig2000, columns = rowHeadersInmig2000)
print(dataInmig2000) 

# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable2000 = []
for i in range(len(tableValuesInmig2000)):
  for h in range(len(rowHeadersInmig2000)):
    newTable2000.append(tableValuesInmig2000[i][h].replace(' [+]', ''))

print(newTable2000)

# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody2000 = np.array(newTable2000).reshape(len(tableValuesInmig2000),len(rowHeadersInmig2000))
InmigBody2000[:1]


## GENERACIÓN DEL DATAFRAME
finalInmig2000 = pd.DataFrame(InmigBody2000, columns=rowHeadersInmig2000)
finalInmig2000.head(1)




### Proceso de scraping para generar el datasets con datos del año 2010

inmig2010 = rqst.get ('https://datosmacro.expansion.com/demografia/migracion/inmigracion?anio=2010')
soupInmig2010 = bs(inmig2010.content, "html.parser")


### Se seleccionan los datos pertenecientes a los nombres de columnas thead 

tableHead2010 = soupInmig2010.thead
print(tableHead2010)

# Se realiza un for para seleccionar los tr y los th y generar una nueva lista con unicacmente los nombres. 
rowHeadersInmig2010 = []

for x in tableHead2010.find_all('tr'):
  for y in x.find_all('th'):
    rowHeadersInmig2010.append(y.text)
rowHeadersInmig2010

### Se seleccionan los datos pertenecientes a los registros con tbody

tableBody2010 = soupInmig2010.tbody
print(tableBody2010)

# Se realiza un for para seleccionar los tr y los td y generar una nueva lista con unicacmente los registros.
tableValuesInmig2010 = []
for x in tableBody2010.find_all('tr')[0:]:
  td_tags = x.find_all('td')
  td_val = [y.text for y in td_tags]
  tableValuesInmig2010.append(td_val)
tableValuesInmig2010[:5]


### Correcciones de datos

# En el paso anterior, se genero una posición vacia ''. Con este procedimiento eliminamos este elemento de cada una de las listas. 
for i in range(len(tableValuesInmig2010)):
  tableValuesInmig2010[i].pop(5)

print(tableValuesInmig2010)

#Visualizamos la información en un dataframe. 
dataInmig2010 = pd.DataFrame(tableValuesInmig2010, columns = rowHeadersInmig2010)
print(dataInmig2010) 

# Se genera un procedimiento para eliminar los [+] de los nombres de paises.
newTable2010 = []
for i in range(len(tableValuesInmig2010)):
  for h in range(len(rowHeadersInmig2010)):
    newTable2010.append(tableValuesInmig2010[i][h].replace(' [+]', ''))

print(newTable2010)

# El procedimiento utilizado para la corrección anterior generó una lista. A esta la convertimos en un numpy.ndarray para estructurar el proyecto.
InmigBody2010 = np.array(newTable2010).reshape(len(tableValuesInmig2010),len(rowHeadersInmig2000))
InmigBody2010[:1]


## GENERACIÓN DEL DATAFRAME
finalInmig2010 = pd.DataFrame(InmigBody2010, columns=rowHeadersInmig2010)
finalInmig2010.head(1)

## ----------------------------------
## Se agrega una columna para cada dataframe con el año correspondiente

## 2000
year2000_list = []
for i in range(194):
  year2000_list.append("2000")
finalInmig2000["year"] = year2000_list

## 2005
year2005_list = []
for i in range(194):
  year2005_list.append("2005")
finalInmig2005["year"] = year2005_list

## 2010
year2010_list = []
for i in range(195):
  year2010_list.append("2010")
finalInmig2010["year"] = year2010_list


## 2015
year2015_list = []
for i in range(195):
  year2015_list.append("2015")
finalInmig2015["year"] = year2015_list

## 2017
year2017_list = []
for i in range(195):
  year2017_list.append("2017")
finalInmig2017["year"] = year2017_list


## 2019
year2019_list = []
for i in range(195):
  year2019_list.append("2019")
finalInmig2019["year"] = year2019_list


## ----------------------------------
## Se agregan las sentencias para exportar los .CSV


## Agrego la sentencia para generar el csv 2000
#finalInmig2000.to_csv('finalInmig2000.csv', encoding='utf-8')

## Agrego la sentencia para generar el csv 2005
#finalInmig2005.to_csv('finalInmig2005.csv', encoding='utf-8')

## Agrego la sentencia para generar el csv 2010
#finalInmig2010.to_csv('finalInmig2010.csv', encoding='utf-8')

## Agrego la sentencia para generar el csv 2015
#finalInmig2015.to_csv('finalInmig2015.csv', encoding='utf-8')

## Agrego la sentencia para generar el csv 2017
#finalInmig2017.to_csv('finalInmig2017.csv', encoding='utf-8')

## Agrego la sentencia para generar el csv 2019
#finalInmig2019.to_csv('finalInmig2019.csv', encoding='utf-8')

## UNIÓN AGRUPADA CON PAISES. UNION HORIZONTAL.
##csv_2000_to_2019 = pd.concat([finalInmig2000, finalInmig2005, finalInmig2010, finalInmig2015, finalInmig2017, finalInmig2019], axis=1)


## UNIÓN VERTICAL, DUPLICANDO PAISES.
csv_2000_to_2019 = pd.concat([finalInmig2000, finalInmig2005, finalInmig2010, finalInmig2015, finalInmig2017, finalInmig2019])
#csv_2000_to_2019.to_csv('csv_2000_to_2019.csv', encoding='utf-8')



