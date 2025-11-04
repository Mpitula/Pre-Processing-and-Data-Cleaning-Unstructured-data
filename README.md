# News Category Dataset Text Cleaning

## 📘 Project Title
**News Category Dataset Cleaning and Preprocessing**

---

## 📄 Description
This project focuses on cleaning and preparing **unstructured text data** from the News Category Dataset (Kaggle).  
The dataset contains news headlines and descriptions across various categories.  
The goal is to clean and tokenize the text for further NLP analysis.

---

## 🧠 Objectives
1. Load the JSON dataset into Pandas.  
2. Remove duplicate records.  
3. Convert text to lowercase.  
4. Remove punctuation and stopwords.  
5. Tokenize text into words.  
6. Save the cleaned version as `news_clean.json`.

---

## ⚙️ Tools & Libraries
- Python  
- Pandas  
- NLTK  
- Regular Expressions (`re`)

---

## 🪜 Steps Performed

### 1. Data Loading
Loaded the dataset using:
```python
pd.read_json("News_Category_Dataset_v3.json", lines=True)

### 2. Removing Duplicates
Removed identical entries using:
```python
    df_news.drop_duplicates(inplace=True)


### 3. Text Normalization
Converted all text columns (headline, short_description) to lowercase.

### 4. Noise Removal

Removed punctuation using Regular Expressions (re.sub).

Removed stopwords using NLTK’s English stopword list.

### 5. Tokenization

Split text into individual words using:
```python
    word_tokenize()

### 6. Exporting Cleaned Data

Saved the cleaned dataset as:
```pgsql
    news_clean.json

📦 Output Files

news_clean.json — cleaned unstructured dataset ready for NLP.