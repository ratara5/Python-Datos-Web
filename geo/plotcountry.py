#STEP 3: Get country geojson n' plot it with layers countries division n' oceans

import geopandas as gpd
import matplotlib.pyplot as plt

#ENTER DESIRE ATTRIBUTE
attrib="Número de bautizados" #doen't see in the column of plot

# Load themtic layer
country1 = 'dataWorld.geojson' #INDICATE A REGION (OR COUNTRY) FOR ANALYSIS, IT WILL BE INTEGER!!!

map_country1 = gpd.read_file(country1)
map_country1.head()

year=2019 #INDICATE A YEAR FOR ANALYSIS, IT WILL BE INTEGER!!!

# Control size figure map
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
 
# Control framin map (geographic area)
ax.axis([-85, -65, -20, 15]) #saving focusing
 
# Control title n' axis
ax.set_title('Perú, '+str(year)+', '+attrib, 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4b3621'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Add legend beside of map
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.2)
 
# Generate n' load map
map_country1.plot(column=attrib, cmap='viridis', ax=ax,
              legend=True, cax=cax, zorder=5)
 
# Load base map countries contours
countries = "resources/Shapes/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"
map_countries = gpd.read_file(countries)
map_countries.plot(ax=ax, color='#9b9b9b', zorder=0)

# Load base map ocean contours
ocean = "resources/Shapes/ne_50m_ocean/ne_50m_ocean.shp"
map_ocean = gpd.read_file(ocean)
map_ocean.plot(ax=ax, color='#0CB7F2', zorder=0)