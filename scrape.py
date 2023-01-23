import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
import json

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

cache = []
def on_data(data: EventData):
    scraped = {
        "job_id": data.job_id, 
        "link": data.link, 
        "apply_link": data.apply_link, 
        "title": data.title, 
        "company": data.company, 
        "place": data.place, 
        "description": data.description, 
        "description_html": data.description_html, 
        "date": data.date
        #"seniority_level": data.seniority_level, 
        #"job_function": data.job_function, 
        #"employment_type": data.employment_type, 
        #"industries": data.industries
    }
    cache.append(scraped)


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path=r'C:\Fonte\chromedriver.exe', # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=0.4,  # Slow down the scraper to avoid 'Too many requests (429)' errors
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        options=QueryOptions(
            locations=['United States'],
            optimize=True,  # Blocks requests for resources like images and stylesheet
            limit=10,  # Limit the number of jobs to scrape
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,                
            )
        )
    ),
]

scraper.run(queries)
import os 
with open(os.getcwd()+'/jobs.json', 'w') as f:
    json.dump(cache, f, indent=4)

print(f"Operation completed. Scraped {len(cache)} jobs")
