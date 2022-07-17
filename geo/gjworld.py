# STEP 2: Generate consolidated geojson
import os
import json as j

countries=[]

#OBTAIN List of countries availables in geojsons: Read files in folder gjCountryYear delete word 'gj' AND APPEND TO countries_by_year_list
content=os.listdir('gjCountryYear')
print(content)
for con in content:
    countries.append(con[2:-12])
year=int(content[0][-12:-8])


#OPEN dataWorld.geojson
with open('dataWorld.geojson') as file:
        data_world = j.load(file)

#CLEAN dataWorld.geojson
data_world["features"].clear()

#SAVE dataWorld.geojson
with open('dataWorld.geojson', 'w') as file:
    j.dump(data_world, file, indent=4)

#FOR COUNTRY
for country in countries:
    with open('gjCountryYear/gj'+country+str(year)+'.geojson') as file:
            data = j.load(file)

    #TODO: COPY ALL geojson BY COUNTRY and CARRIE TO dataWorldYear Year(?)
    data_world["features"].append(data)

    with open('dataWorld.geojson', 'w') as file:
        j.dump(data_world, file, indent=4)
