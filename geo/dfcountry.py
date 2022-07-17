#STEP 0: Obtain info of df by Country from .csv
import pandas as pd

#GET COUNTRY NAME OR COUNTRIES LIST BY REGION (?)
country="Perú"

#GET YEARS LIST
years=['2017','2018','2019','2020']

#GET COLUMNS TO SHOW
columns=['Habitantes','Máximo de publicadores','Un publicador por cada','Promedio de publicadores','Porcentaje de aumento sobre','Número de bautizados','Promedio de precursores','Número de congregaciones','Asistencia a la conmemoración']

#dfCountry INITIALIZES EMPTY
globals()['df'+country]=pd.DataFrame()
for year in years:

    #GET DATAFRAME ROW FROM CSV (CSV OBTAINED BY SCRAPING IN OTHER SCRIPT)
    globals()['df'+year]=pd.read_csv('dfYear/df'+year+'.csv',index_col="Unnamed: 0")
    globals()['df'+year+country]=globals()['df'+year].loc[[country]] #only one '[' returns Serie, two '[' returns DataFrame

    #NORMALIZE COLUMNS WITH DIFFERENT NAMES
    #Columns with different names. Don't contain year 
    if year=='2017' or year=='2018':
        globals()['df'+year+country]=globals()['df'+year+country].rename(columns={"Proporción, un publicador por cada:":"Un publicador por cada"}) 
    
    #Columns with different names. Contain year 
    dfCols=globals()['df'+year+country].columns
    if year=="2017" or year=="2018":
        cols=columns.copy()
        del cols[3] #Delete a column name that doesn't exit in year 2017 and 2018
        globals()['df'+year+country]=globals()['df'+year+country].rename(columns={dfCol:col for dfCol,col in zip (dfCols,cols)}) 
    else:
        globals()['df'+year+country]=globals()['df'+year+country].rename(columns={dfCol:col for dfCol,col in zip (dfCols,columns) })

    #RENAME INDEX. WILL BE YEAR
    globals()['df'+year+country]=globals()['df'+year+country].rename(index={country:year})
    
    #CONCAT BEFORE WITH NEW DATAFRAME ROW
    globals()['df'+country]=pd.concat([globals()['df'+country],globals()['df'+year+country]],axis=0)

#PRINT DATAFRAME OF COUNTRY
print(globals()['df'+country].iloc[:,0:3])

#SAVE DATAFRAME OF COUNTRY AS CSV
globals()['df'+country].to_csv('dfCountry/df{}.csv'.format(country)) 