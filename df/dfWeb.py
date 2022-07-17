# #STEP 0: Obtain info of df by Country from .csv
import pandas as pd
import os

class FactoryDF():
    def __init__(self,directory,col_erase):
        self.directory=directory
        self.col_erase=col_erase

    def load_primary_df(self): #returns dictionary which KEY is YEAR and which VALUE is DATAFRAME FOR THE RESPECTIVE YEAR
        years=[cont[-8:-4] for cont in os.listdir(self.directory)]
        dict_df_prim={year:pd.read_csv(self.directory+'/df'+year+'.csv',index_col=self.col_erase) for year in years}
        return dict_df_prim 

    def get_colums(self): #returns dictionary year:columns 
        dict_df_prim=self.load_primary_df()
        years=dict_df_prim.keys()
        dict_columns={year:dict_df_prim[year].columns for year in years}
        return dict_columns

    def get_country_df(self,country,columns): #returns dataframe by country for enter columns 
        dict_df_prim=self.load_primary_df()
        years=dict_df_prim.keys()
        country_df=pd.DataFrame()        
        for year in years:
            country_year_df=dict_df_prim[year].loc[[country]]
            df_cols=country_year_df.columns         
            if len(df_cols)<len(columns):
                print('PRECAUCIÓN: El df de '+year+' tiene menor cantidad de columnas que la entrada')
                #ingresar números de columna a agregar
                num_col=3
                df_cols=[column for column in country_year_df.columns]
                df_cols.insert(3,columns[num_col])
            country_year_df=country_year_df.rename(columns={df_col:col for df_col,col in zip (df_cols,columns)}) #This doesn´t work, because a column name does'nt exist in 2017 and 2018
            country_year_df=country_year_df.rename(index={country:year})
            country_df=pd.concat([country_df,country_year_df],axis=0)
        country_df.to_csv('dfCountry/df{}.csv'.format(country)) 
        print('AVISO: Se ha generado el df'+country+' en la ubicación /dfCountry/')
        return country_df
               

factory_DF=FactoryDF('dfYear', "Unnamed: 0")
dict_DF=factory_DF.load_primary_df()
#print(dict_DF['2020']) #Get a df by year, year is KEY of a dataframes dictionary

dict_columns=factory_DF.get_colums()
#print(dict_columns) #Get columns for analyze. Then in the next line, enter columns which is list of max columns

columns=['Habitantes','Máximo de publicadores','Un publicador por cada','Promedio de publicadores','Porcentaje de aumento sobre','Número de bautizados','Promedio de precursores','Número de congregaciones','Asistencia a la conmemoración']

colombia_df=factory_DF.get_country_df('Colombia',columns)
print(colombia_df)

# #GET COUNTRY NAME
# country="México"

# #GET YEARS LIST
# years=['2017','2018','2019','2020']

# #GET COLUMNS TO SHOW
# columns=['Habitantes','Máximo de publicadores','Un publicador por cada','Promedio de publicadores','Porcentaje de aumento sobre','Número de bautizados','Promedio de precursores','Número de congregaciones','Asistencia a la conmemoración']

# #dfCountry INITIALIZES EMPTY
# globals()['df'+country]=pd.DataFrame()
# for year in years:

#     #GET DATAFRAME ROW FROM CSV (CSV OBTAINED BY SCRAPING IN OTHER SCRIPT)
#     globals()['df'+year]=pd.read_csv('df'+year+'.csv',index_col="Unnamed: 0")
#     globals()['df'+year+country]=globals()['df'+year].loc[[country]] #only one '[' returns Serie, two '[' returns DataFrame

#     #NORMALIZE COLUMNS WITH DIFFERENT NAMES
#     #Columns with different names. Don't contain year 
#     if year=='2017' or year=='2018':
#         globals()['df'+year+country]=globals()['df'+year+country].rename(columns={"Proporción, un publicador por cada:":"Un publicador por cada"}) 
    
#     #Columns with different names. Contain year 
#     dfCols=globals()['df'+year+country].columns
#     if year=="2017" or year=="2018":
#         cols=columns.copy()
#         del cols[3] #Delete a column name that doesn't exit in year 2017 and 2018
#         globals()['df'+year+country]=globals()['df'+year+country].rename(columns={dfCol:col for dfCol,col in zip (dfCols,cols)}) 
#     else:
#         globals()['df'+year+country]=globals()['df'+year+country].rename(columns={dfCol:col for dfCol,col in zip (dfCols,columns) })

#     #RENAME INDEX. WILL BE YEAR
#     globals()['df'+year+country]=globals()['df'+year+country].rename(index={country:year})
    
#     #CONCAT BEFORE WITH NEW DATAFRAME ROW
#     globals()['df'+country]=pd.concat([globals()['df'+country],globals()['df'+year+country]],axis=0)

# #PRINT DATAFRAME OF COUNTRY
# print(globals()['df'+country].iloc[:,0:3])

# #SAVE DATAFRAME OF COUNTRY AS CSV
# globals()['df'+country].to_csv('df{}.csv'.format(country)) 