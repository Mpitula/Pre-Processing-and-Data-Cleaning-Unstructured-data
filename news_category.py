import pandas as pd
import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 1. Download stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


# 2. Load the JSON dataset (ensure you have the file locally)
df_news = pd.read_json("JSON_Files/News_Category_Dataset_v3.json", lines=True)
# Display the first few rows of the dataframe
print(df_news.head())
print("Dataset loaded successfully!")
print(f"Number of rows before cleaning: {df_news.shape[0]}")

# 3. Remove duplicates
df_news = df_news.drop_duplicates(subset=["headline", "short_description"])
print(f"Rows after removing duplicates: {df_news.shape[0]}")

# 4. Convert text to lowercase
df_news["headline"] = df_news["headline"].str.lower()
df_news["short_description"] = df_news["short_description"].str.lower()

# 5. Remove punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

df_news["headline"] = df_news["headline"].apply(remove_punctuation)
df_news["short_description"] = df_news["short_description"].apply(remove_punctuation)

# 6. Remove stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = word_tokenize(text)
    filtered = [word for word in words if word not in stop_words]
    return " ".join(filtered)

df_news["headline"] = df_news["headline"].apply(remove_stopwords)
df_news["short_description"] = df_news["short_description"].apply(remove_stopwords)

# 7. Tokenize text into individual words
df_news["headline_tokens"] = df_news["headline"].apply(word_tokenize)
df_news["description_tokens"] = df_news["short_description"].apply(word_tokenize)


# 8. Save the cleaned version as JSON
df_news.to_json("JSON_Files/cleaned_news_clean.json", orient="records", lines=True)
print("Saved cleaned JSON as 'cleaned_news_clean.json'")

with open("JSON_Files/cleaned_news_clean.json", "r", encoding="utf-8") as f:
    lines = f.read()
print(json.dumps(json.loads(lines.splitlines()[0]), indent=4, ensure_ascii=False))
print("Sample of cleaned data:")
print(df_news.head())
