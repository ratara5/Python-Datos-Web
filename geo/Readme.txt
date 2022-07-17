STEP 0: IN: Worlds dataframes by year [.csv] in folder /dfYear
	OUT: Country dataframe by year lapse [.csv] in folder /dfCountry

STEP 1: IN: Countries dataframes by year lapse [.csv] in folder /dfCountry
	OUT: Country geojson by year [.geojson] in folder /gjCountryYear

STEP 2: IN: Countries geojson by year [.geojson] in folder /gjCountryYear
	OUT: dataWorld with saved countries [.geojson] in folder root 

STEP 3: IN: dataWorld with saved countries [.geojson] in folder root
	OUT: plot on world map of selected attribute by country by year
