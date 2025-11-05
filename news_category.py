import pandas as pd
import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Step 2: Load the JSON dataset (ensure you have the file locally)
df_news = pd.read_json("JSON_Files/News_Category_Dataset_v3.json", lines=True)
# Display the first few rows of the dataframe
print(df_news.head())
print("Dataset loaded successfully!")
print(f"Number of rows before cleaning: {df_news.shape[0]}")