import pandas as pd
import json

### Load into pandas

# Load JSON data into a DataFrame
df_news = pd.read_json("News_Category_Dataset_v3.json", lines=True)

# Display first few rows
print(df_news.head())

# Check basic info
print(df_news.info())

## Removed identical entries using 'headline' and 'short_description'

df_news_unique = df_news.drop_duplicates(subset=['headline', 'short_description'])
print(f"Original entries: {len(df_news)}, Unique entries: {len(df_news_unique)}")
df_news = df_news_unique
print(df_news.info())


df_news['headline'] = df_news['headline'].str.lower()
df_news['short_description'] = df_news['short_description'].str.lower()
df_news['category'] = df_news['category'].str.lower()
print(df_news.head())


import re
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)     # remove punctuation
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

df_news['headline'] = df_news['headline'].apply(clean_text)
df_news['short_description'] = df_news['short_description'].apply(clean_text)
df_news['category'] = df_news['category'].apply(clean_text)
print(df_news.head())

from nltk.tokenize import word_tokenize
df_news['headline_tokens'] = df_news['headline'].apply(word_tokenize)
df_news['short_description_tokens'] = df_news['short_description'].apply(word_tokenize)
df_news['category_tokens'] = df_news['category'].apply(word_tokenize)
print(df_news.head())

# Save cleaned data to a new JSON file
df_news.to_json("news_clean.json", orient='records', lines=True)

