import time
from typing import KeysView

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import openpyxl as xl
import pandas as pd

from getpass import getuser

options=webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:/Users/{}/AppData/Local/Google/Chrome/User DataDefault'.format(getuser()))
options.add_argument('--profile-directory=Default')
#options.add_argument('--headless')

#INSTANCE WEBDRIVER
chrome_browser=webdriver.Chrome(executable_path=r'C:/Users/{}/VscodeFiles/python/infosTj/driver/chromedriver.exe'.format(getuser()),options=options) 

#SURF TO WEB
chrome_browser.get('https:www.jw.org/es/biblioteca/libros')

#LIST: Identify Webelements
input =WebDriverWait(chrome_browser,10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="pubFilter"]')))
inputClick=WebDriverWait(chrome_browser, 15).until(EC.element_to_be_clickable(input)); #The class Select doesn't work
input.click()

#LIST: Write Content
years=['2017','2018','2019','2020','2021'] #value of <option> is equal to 'syrnn' where nn=two last digits of year. 
#for year in years: (ident all it follows)
    #if year='2017'|'2018'|'2019':
        #input.send_keys("Informe mundial del año de servicio {} de los testigos de Jehová".format(years[0]))
    #else the next line, then as follows
input.send_keys("Informe mundial de los testigos de Jehová del año de servicio {}".format(years[3]))
input.send_keys(Keys.ENTER)

#LIST: Send Content(SEARCH)
chrome_browser.find_element(By.XPATH, '//input[@value="Buscar"]').click()

#PUBLICATION
pubDiv =WebDriverWait(chrome_browser,10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="publicationDesc"]'))) #clickable(?)
pub=chrome_browser.find_element(By.XPATH, '//div[@class="publicationDesc"]').click()

#PUBLICATION CONTENT
pubContentDiv =WebDriverWait(chrome_browser,10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="syn-body sqs   "]'))) #clickable(?)
#if year='2017'|'2018'|'2019':
    #infoBuscar='Informe por países y territorios del {}'.format(years[0])
#else the next line, then as follows
infoBuscar='Informe del {} por países y territorios'.format(years[3]) #use find_by_link_text
chrome_browser.find_element(By.XPATH, "//a[contains(text(), '{}')]".format(infoBuscar)).click()

#GET TABLE VALUES
WebDriverWait(chrome_browser,10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="tableDiv stripe wide gridlines"]')))

rows=chrome_browser.find_elements(By.TAG_NAME,'tr')
cols=chrome_browser.find_elements(By.TAG_NAME,'th')

#Shape
rowsCount=len(rows) #not include +1 what is head
colsCount=len(cols)
print(str(rowsCount+1)+"x"+str(colsCount))

#Heads, ie, columns titles
mc=[]
for i in range(0,colsCount):
    mc.append(cols[i].text)

#rows
mr=[]
for i in range(1,rowsCount):
    r=[]
    row=rows[i]
    for j in range(0,colsCount):
        col=row.find_elements(By.TAG_NAME,'td')[j]
        r.append(col.text)
    mr.append(r)
