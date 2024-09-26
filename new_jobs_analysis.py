#%%
import pandas as pd
path = "./data"
import glob
from os import listdir
from os.path import isfile, join
#csv_files = [f for f in os.listdir(path) if f.startswith('data_analyst')]
#csv_files

csv_files = glob.glob("./data/data_analyst*.csv")

df_list = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames into a single DataFrame
#%%

#%%
combined_df = pd.concat(df_list, ignore_index=True)
#%%

#%%
import re
keywords = ['business systems','intern', 'freelance', 'data entry','business intelligence','data engineer','trainee','warehouse','80%','sql','lead','manager','coordinator','entry level','developer','engineer','online data analyst','bi analyst','contract','controller','associate','graduate','summer','entry-level','winter','apprenticeship','tiktok','java','premaster','engenharia']

# Create a regex pattern to match any of the keywords
pattern = '|'.join(keywords)

# Filter out rows where 'title' contains any of the keywords (case insensitive)
filtered_df = combined_df[~combined_df['Title'].str.contains(pattern, case=False, na=False)]


keywords_lower = ['python','sql','r', 'tableau', 'power bi','azure','google cloud','databricks','git','aws','nosql','spark','docker','gcp','looker','etl','snowflake','redshift','excel','sas','javascript']
#all_data['Description'].str.lower().str.contains(keywords_lower).astype(int)
# iterate over the keywords and create a new column for each keyword
for keyword in keywords_lower:
    filtered_df[keyword] = filtered_df['Description'].str.lower().str.contains(keyword).astype(int)
#filtered_df.to_clipboard(index=False)
#%%
#%%
import spacy

languages = pd.read_csv('./setup/languages.csv')
platforms = pd.read_csv('./setup/platforms.csv')
databases = pd.read_csv('./setup/databases.csv')
frameworks_tools = pd.read_csv('./setup/frameworks_tools_etc.csv')
patterns = []
for x in languages.name.tolist():
    patterns.append({"label": "PROG_LANG", "pattern": [{"lower": w.lower()} for w in str(x).split()],"id": "SKILLS"})

for x in databases.name.tolist():
    patterns.append({"label": "DB","pattern": [{"lower": w.lower()} for w in str(x).split()], "id": "SKILLS"})

for x in platforms.name.tolist():
    patterns.append({"label": "PLATFORM", "pattern": [{"lower": w.lower()} for w in str(x).split()], "id": "SKILLS"})

for x in frameworks_tools.name.tolist():
    patterns.append({"label": "FRAMEWORKS", "pattern": [{"lower": w.lower()} for w in str(x).split()], "id": "SKILLS"})

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = "./setup/patterns.jsonl"
ruler.from_disk(patterns)
#%%

#%%
def extract_tech(description):
    doc = nlp(description)
    frameworks, databases, platforms, prog_langs = [], [], [], []

    for entity in doc.ents:
        if entity.ent_id_ == 'SKILLS':
            if entity.label_ == 'PROG_LANG' and entity.text not in prog_langs:
                prog_langs.append(entity.text)
            if entity.label_ == 'PLATFORM' and entity.text not in platforms:
                platforms.append(entity.text)
            if entity.label_ == 'DB' and entity.text not in databases:
                databases.append(entity.text)
            if entity.label_ == 'FRAMEWORKS' and entity.text not in frameworks:
                frameworks.append(entity.text)

    #prog_langs = " ".join(prog_langs)
    #platforms = " ".join(platforms)
    #databases = " ".join(databases)
    #frameworks = " ".join(frameworks)
    data = (prog_langs, platforms, databases, frameworks)
    data = tuple([x for x in data if x])
    if data:
        return data
    else:
        return None

filtered_df['keywords'] = filtered_df['Description'].apply(extract_tech)
#%%