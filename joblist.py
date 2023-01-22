from selenium import webdriver
import time
import pandas as pd
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url1="https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
y=driver.find_elements_by_class_name('results-context-header__job-count')[0].text

from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(executable_path=r'C:\Users\rafae\OneDrive\Documentos\.wdm\drivers\geckodriver\win64\v0.32.0\geckodriver.exe', options=options)
driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get(url1)
i = 2
while i <= int((n+200)/25)+1: 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    
    try:
        send=driver.find_element_by_xpath("//button[@aria-label='Load more results']")
        driver.execute_script("arguments[0].click();", send)   
        time.sleep(3)
    
        
         #buu=driver.find_elements_by_tag_name("button")
         #x=[btn for btn in buu if btn.text=="See more jobs"]
         #for btn in x:
                #driver.execute_script("arguments[0].click();", btn)
                #time.sleep(3)
        
                                                 


            
    except:
        pass
        time.sleep(5)
         
         
companyname= []
titlename= []

try:
    for i in range(n):
        company=driver.find_elements_by_class_name('base-search-card__subtitle')[i].text
        companyname.append(company)
        
            
    

        
    

    
    
except IndexError:
    print("no")
    
company    
    
try:
    for i in range(n):
        
        
        title=driver.find_elements_by_class_name('base-search-card__title')[i].text
    

        titlename.append(title)
        
            


    
    
except IndexError:
    print("no")

len(titlename)
companyfinal=pd.DataFrame(companyname,columns=["company"])
titlefinal=pd.DataFrame(titlename,columns=["title"])
n=pd.to_numeric(y)

x=companyfinal.join(titlefinal)

