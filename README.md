You can copy and save this as README.md in your project folder.

# 📰 News Category Dataset Cleaning and Preprocessing

## 📘 Project Title
**News Category Dataset (Unstructured Data Cleaning)**

---

## 📄 Description
This project focuses on cleaning and preprocessing **unstructured text data** from the [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) by Rishabh Misra.  
The dataset contains news headlines and short descriptions across multiple categories.  
The goal of this project is to prepare the text for **Natural Language Processing (NLP)** tasks such as sentiment analysis, topic modeling, or classification.

---

## 🧠 Objectives
1. Load the JSON dataset into Pandas.  
2. Remove duplicate records.  
3. Convert all text to lowercase.  
4. Remove punctuation and stopwords.  
5. Tokenize text into individual words.  
6. Save the cleaned version as `news_clean.json`.

---

## ⚙️ Tools & Libraries Used
- **Python**  
- **Pandas** — for data loading and manipulation  
- **NLTK** — for text preprocessing and tokenization  
- **Regular Expressions (re)** — for removing punctuation and symbols  

---

## 🪜 Steps Performed
```python
### 1. Load the Dataset
Loaded the JSON dataset using Pandas:

import pandas as pd
df_news = pd.read_json("News_Category_Dataset_v3.json", lines=True)

### 2. Remove Duplicates

Dropped all duplicate records to ensure data consistency:

df_news.drop_duplicates(inplace=True)

### 3. Convert Text to Lowercase

Standardized text to lowercase for uniformity:

df_news['headline'] = df_news['headline'].str.lower()
df_news['short_description'] = df_news['short_description'].str.lower()

### 4. Remove Punctuation and Stopwords

Used Regular Expressions and NLTK to clean the text:

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

### 5. Tokenize Text

Split text into individual words (tokens):

from nltk.tokenize import word_tokenize
df_news['headline_tokens'] = df_news['headline'].apply(word_tokenize)
df_news['short_description_tokens'] = df_news['short_description'].apply(word_tokenize)

### 6. Save the Cleaned Dataset

Exported the cleaned version of the dataset:

df_news.to_json("news_clean.json", orient='records', lines=True)

### 📦 Output Files

news_clean.json → Final cleaned dataset ready for NLP analysis.

## 📊 Summary
Step	Issue Identified	Action Taken
Duplicates	Multiple identical rows	Removed using drop_duplicates()
Text Case	Mixed uppercase/lowercase	Converted to lowercase
Punctuation	Presence of symbols and marks	Removed using Regular Expressions
Stopwords	Frequent common words	Removed using NLTK stopwords
Tokenization	Continuous text	Split into tokens using word_tokenize()

