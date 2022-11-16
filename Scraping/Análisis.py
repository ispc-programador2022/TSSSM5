# Importo las librerias necesarias. 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
import matplotlib.ticker as mtick


mpl.style.use('bmh')

# Importo el CSV generado mediante scraping.

df_complete = pd.read_csv(r'/TSSSM5/Scraping/finalInmig2015.csv')

# Cantidad de filas y columnas
df_complete.shape

# Encabezado de la tabla y primeros 5 registros.
df_complete.head(5)

# Nombre de columnas
df_complete.columns

# Informacion sobre tipo
df_complete.info()

# Por cada columna a modificar realizo un ciclo FOR.

# Reemplazo los "." por espacios vacios.
Inmigrants_total = []
for h in range(len(df_complete["Inmigrantes"])):
    Inmigrants_total.append(int(df_complete["Inmigrantes"][h].replace('.', '')))

# Reemplazo los "." por espacios vacios.
Inmigrants_m_total = []
for h in range(len(df_complete["Inmigrantes mujeres"])):
    Inmigrants_m_total.append(int(df_complete["Inmigrantes mujeres"][h].replace('.', '')))

# Reemplazo los "." por espacios vacios.
Inmigrants_h_total = []
for h in range(len(df_complete["Inmigrantes hombres"])):
    Inmigrants_h_total.append(int(df_complete["Inmigrantes hombres"][h].replace('.', '')))

# Reemplazo los "." y "%" por espacios vacios. 
Inmigrants_porc_total = []
for h in range(len(df_complete['% Inmigrantes'])):
    Inmigrants_porc_total.append(float(df_complete['% Inmigrantes'][h].replace('%', '').replace(',', '.')))

# Convierto a string los años.
Inmigrants_year_total = []
for h in range(len(df_complete["year"])):
    Inmigrants_year_total.append(str(df_complete["year"][h]))

# Agrego al DataFrame las columnas corregidas.
df_complete["Inmigrantes_total"] = Inmigrants_total
df_complete["Inmigrantes_hombres"] = Inmigrants_m_total
df_complete["Inmigrantes_mujeres"] = Inmigrants_h_total
df_complete["Proporcion_total"] = Inmigrants_porc_total
df_complete["Year"] = Inmigrants_year_total

# Elimino las columnas erroneas.
df_complete = df_complete.drop(['% Inmigrantes','Inmigrantes hombres','Inmigrantes mujeres', 'Inmigrantes', 'year'], axis=1)

# Muestro la estructura de la tabla final.
df_complete.head(10)

# Genero un DataFrame agrupando los inmigrantes por año y elimino las columnas innecesarias.
cant_year = df_complete.groupby(["Year"]).sum('Inmigrantes_total')
cant_year = cant_year.drop(['Unnamed: 0', 'Proporcion_total'], axis=1)

# Visualizo la tabla con los datos grupados por año. 
cant_year.head()

# Realizo un grafico indexando los años.
year_index = cant_year.index

fig, ax = plt.subplots(figsize=(16,6))
ax.plot(year_index, cant_year["Inmigrantes_total"], 'b',  label='Inmigraciones')
ax.plot(year_index, cant_year["Inmigrantes_total"],  'b+')
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_xlabel('Año')                  
ax.set_ylabel('Cantidad')
ax.set_title('Evolución de las inmigraciones 2000 - 2019')
ax.legend() 

## Enfocamos en los años 2000 y 2019:

## Creo un dataframe con los registros pertenecientes al año 2000
df_2000 = df_complete[df_complete['Year'] == '2000']

## Creo un dataframe con los registros pertenecientes al año 2019
df_2019 = df_complete[df_complete['Year'] == '2019']

## El dataframe del año 2000 cuenta con las siguiente cantidad de filas y columnas:
# Cantidad de filas y columnas
df_2000.shape

## El dataframe del año 2019 cuenta con las siguiente cantidad de filas y columnas:
# Cantidad de filas y columnas
df_2019.shape

## Genero los siguientes gráficos que muestran los 10 paises con mayor inmigración para los años 2000 y 2019.
# Para ambos años ordeno el dataframe según cantidad de inmigrantes en orden descendente.
df_2000 = df_2000.sort_values(by=['Inmigrantes_total'], ascending=False)
top_10_df_2000 = df_2000.head(10)

df_2019 = df_2019.sort_values(by=['Inmigrantes_total'], ascending=False)
top_10_df_2019 = df_2019.head(10)

# Gráfico 2000
fig, ax = plt.subplots(figsize=(16,6))
ax.barh(top_10_df_2000['Países'], top_10_df_2000['Inmigrantes_total'])
ax.set_title('Top 10 total de Inmigraciones por país. Año 2000')
ax.set_ylabel('Países')
ax.set_xlabel('Total en millones')

# Gráfico 2019
fig, ax = plt.subplots(figsize=(16,6))
ax.barh(top_10_df_2019['Países'], top_10_df_2019['Inmigrantes_total'])
ax.set_title('Top 10 total de Inmigraciones por país. Año 2019')
ax.set_ylabel('Países')
ax.set_xlabel('Total en millones')

plt.show()

## A su vez, muestro en los siguientes gráficos el TOP 10 paises con mayor proporción de inmigrantes sobre su población total.
# Para ambos años ordeno el dataframe según la proporción de inmigrantes sobre el total de la población en orden descendente.

df_2000_sort =df_2000.sort_values(by=['Proporcion_total'], ascending=False)
top_10_prop_inm_2000 = df_2000_sort.head(10)

df_2019_sort =df_2019.sort_values(by=['Proporcion_total'], ascending=False)
top_10_prop_inm_2019 = df_2019_sort.head(10)

# Gráfico 2000
fig, ax = plt.subplots(figsize=(16,6))
ax.barh(top_10_prop_inm_2000['Países'], top_10_prop_inm_2000['Proporcion_total'])
ax.set_title('Top 10 proporcion total de inmigrantes por país. Año 2000')
ax.set_ylabel('Países')
ax.set_xlabel('Proporción total')

# Gráfico 2019
fig, ax = plt.subplots(figsize=(16,6))
ax.barh(top_10_prop_inm_2019['Países'], top_10_prop_inm_2019['Proporcion_total'])
ax.set_title('Top 10 proporcion total de inmigrantes por país. Año 2019')
ax.set_ylabel('Países')
ax.set_xlabel('Proporción total')

## En cuanto a la frecuencia de proporción de inmigrantes sobre su población total para los años 2000 y 2019 genero histogramas:
# Gráfico histograma 2000
fig, ax = plt.subplots(figsize=(16,6))
ax.hist(df_2000['Proporcion_total'], 10, alpha=0.75)
ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
ax.set_xlabel('Proporción')                  
ax.set_ylabel('Cantidad')
ax.set_title('Histograma de frecuencias de proporcion de inmigración. Año 2000')

# Gráfico histograma 2019
fig, ax = plt.subplots(figsize=(16,6))
ax.hist(df_2019['Proporcion_total'],10, alpha=0.75)
ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
ax.set_xlabel('Proporción')                  
ax.set_ylabel('Cantidad')
ax.set_title('Histograma de frecuencias de proporcion de inmigración. Año 2019')
plt.show()

## Acerca de la situación de Argentina
## Cantidad de inmigrantes según año.
# DataFrame con registros de Argentina.
arg_inmig = df_complete[df_complete['Países'] == 'Argentina']
arg_inmig = arg_inmig.drop(['Unnamed: 0'], axis=1)
arg_inmig.head(6)

# Gráfico temporal Argentina
fig, ax = plt.subplots(figsize=(16,6))
ax.plot(arg_inmig["Year"], arg_inmig["Inmigrantes_total"], 'b',  label='Inmigraciones en Argentina')
ax.plot(arg_inmig["Year"], arg_inmig["Inmigrantes_total"],  'b+')
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_xlabel('Año')                  
ax.set_ylabel('Cantidad')
ax.set_title('Argentina: Evolución de las inmigraciones 2000 - 2019')
ax.legend() 

## Cantidad de inmigrantes según genero y año en Argentina.
#Grafico de columnas horizontales.
fig, ax = plt.subplots(figsize=(16,10))
ax.barh(arg_inmig["Year"], arg_inmig["Inmigrantes_hombres"], label = 'Inmigrantes hombres')
ax.barh(arg_inmig["Year"], arg_inmig["Inmigrantes_mujeres"], label = 'Inmigrantes mujeres')
ax.set_title('Proporcion de inmigrantes mujeres y hombres')
ax.set_ylabel('Año')
ax.set_xlabel('Cantidad total. En millones')
plt.legend()
plt.show()

