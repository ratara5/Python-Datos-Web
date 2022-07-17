#STEP 1: Give info statistic from dfyear to geojson
import os
import pandas as pd
import json as j

year=2019 #INDICATE A YEAR FOR ANALYSIS, IT WILL BE INTEGER!!!
countries=[]

#OBTAIN List of countries availables in dataframes: read files in folder dfCountry delete word 'df' AND APPEND TO countries_list #IGNORE FOLDERS
#content=os.listdir('C:/Users/{}/VscodeFiles/python/geo/dfCountry')
content=os.listdir('dfCountry')
print(content)
for con in content:
    countries.append(con[2:-4])

#FOR COUNTRY
for country in countries:
    
    #OBTAIN df OF THE COUNTRY
    df=pd.read_csv('dfCountry/df'+country+'.csv', index_col="Unnamed: 0")
    atr_dict={colum:df.loc[year,colum] for colum in df.columns}
    print(atr_dict)
    atr_items = atr_dict.items()

    #OBTAIN geojson OF THE COUNTRY (FILENAMES ARE IN SPANISH!!!)
    with open('resources/GeoJson countries/'+country+'.geojson') as file:
        data = j.load(file)

    #WRITE df TO GEOJSON
    for key, value in atr_items:
        data['properties'][key]=value
    print(data['properties'])

    #SAVE NEW GEOJSON
    with open('gjCountryYear/gj'+country+str(year)+'.geojson', 'w') as file:
        j.dump(data, file, indent=4)