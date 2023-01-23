import collections
import pandas as pd
import matplotlib.pyplot as plt

wordcount = {}

df = pd.read_csv('Job_Postings.csv')

print(df.head())

for text in df['Description']:
    for word in text.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

word_counter = collections.Counter(wordcount)

ls = word_counter.most_common()
