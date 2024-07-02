#%%
import pandas as pd
from time import gmtime,strftime
from selenium import webdriver
import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, OnSiteOrRemoteFilters
import json
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
#%%

#
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
chrome_options = webdriver.ChromeOptions() 

options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)
    
driver = webdriver.Chrome(options = chrome_options)
#%%

#%%
# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

# cache = []
# def on_data(data: EventData):
#     scraped = {
#         "job_id": data.job_id, 
#         "link": data.link, 
#         "apply_link": data.apply_link, 
#         "title": data.title, 
#         "company": data.company, 
#         "place": data.place, 
#         "description": data.description, 
#         "description_html": data.description_html, 
#         "date": data.date
#         #"seniority_level": data.seniority_level, 
#         #"job_function": data.job_function, 
#         #"employment_type": data.employment_type, 
#         #"industries": data.industries
#     }
#     cache.append(scraped)
    
job_postings = []
def on_data(data: EventData):
    job_postings.append([data.job_id,data.link,data.apply_link,data.title,data.company,data.place,data.description,data.description_html,data.date,
                         data.seniority_level,data.job_function,data.employment_type,data.industries])

def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    #chrome_executable_path=r'C:\Fonte\chromedriver.exe', # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_executable_path=None,
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=1.2  # Slow down the scraper to avoid 'Too many requests (429)' errors
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

#%%

#%%
group_of_items = {'Seattle, Washington, United States',
'San Francisco, California, United States',
'United States Remote','European Union Remote',
'Boston, Massachusetts, United States',
'Berlin, Germany',
'London, England, United Kingdom',
'Canada Remote',
'Toronto, Ontario, Canada',
'Vancouver, British Columbia, Canada',
'Madrid, Community of Madrid, Spain',
'Barcelona, Catalonia, Spain',
'Spain'
}
num_to_select = 1
locationsToQuery = random.sample(sorted(group_of_items), num_to_select)

query_1 = [
    Query(
      query='Data Analyst',
        options=QueryOptions(
            locations=locationsToQuery,
            #optimize=True,  # Blocks requests for resources like images and stylesheet
            limit=3,  # Limit the number of jobs to scrape
            skip_promoted_jobs=True,
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
                #type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None               
            )
        )
    ),
]

scraper.run(query_1)
# with open('data/jobs.json', 'w') as f:
#     json.dump(cache, f, indent=4)
# print(f"Operation completed. Scraped {len(cache)} jobs")
#%%

#%%
df = pd.DataFrame(job_postings,columns=['Job_ID','Link','Apply Link','Title','Company','Place','Description','HTML','Date','Seniority Level','Job Function','Employment Type','Industries'])
#%%

#%%
df.to_csv('./data/data_analyst_'+strftime("%Y%m%d", gmtime())+'.csv',index=False)
#%%

##### TRYING TO OBTAIN INFO FOR DATA SCIENTIST POSITIONS #####
job_postings = []
query_2 = [
    Query(
      query='Data Scientist',
        options=QueryOptions(
            locations=locationsToQuery,
            #optimize=True,  # Blocks requests for resources like images and stylesheet
            limit=3,  # Limit the number of jobs to scrape
            skip_promoted_jobs=True,
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
                #type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None               
            )
        )
    ),
]

scraper.run(query_2)
#%%
df2 = pd.DataFrame(job_postings,columns=['Job_ID','Link','Apply Link','Title','Company','Place','Description','HTML','Date','Seniority Level','Job Function','Employment Type','Industries'])
#%%

#%%
df2.to_csv('./data/data_scientist_'+strftime("%Y%m%d", gmtime())+'.csv',index=False)
#%%
