# In-demand skills for Data Analysts according to thousands of job ads

A study on the skills required by companies for Data Analysts (at least from what they say in their job ads) - based in 20K job ads scraped from Linkedin.

Some preliminary results:
https://rafabelokurows.github.io/data-analyst-job-skills/

## Goals

Obtain a large pool of job ad descriptions found on Linkedin to answer a few burning questions for me and fellow Data Analysts:
 - What are the skills most in demand (R, SQL, Python, etc.)?  
 - How about salary? 💲💲💲 What's the distribution of salaries a Data Analyst can expect for a remote job?  
 - Is there any difference in the skills asked for a job in the US x Europe?  
 - How about those good old cliches that you hate to find on a job ad and that makes you wanna cringe?  
"We look for a *detail-oriented* *multi-tasker* who can work *under pressure* on a *fast-paced environment*"  

## Roadmap

- [x] Set up a pipeline to process new data scraped from Linkedin
- [x] Create some plots of skills, salary and Europe x Americas
- [ ] Expand keywords to roles such as "Product Analyst", "Analytics Engineer", and others
- [ ] Cluster similar positions based on main types of activities: Governance, Analysis, Scientific/Research
- [x] Train ML models to predict salary based on skills, requisites and other characteristics of the job
- [x] Add automated collection workflow running on Github Actions

## References
Some of my references for this one:
https://github.com/peuvitor/portfolio/blob/f3bfcfbc26432682cfdf93122ab221027ea1578e/docs/projects/de/scraping-jobs.md
https://pypi.org/project/linkedin-jobs-scraper/
https://github.com/newlog/linkedin_job_analysis/tree/3ed8946d0ce8bcae5bf0c383534d8c3fb81b7aee/src
https://github.com/zejiekong/JobScore/blob/c801603bd1a67e78bd39a5019eb2016d4fe160f1/helper/scrape_linkedin.py



