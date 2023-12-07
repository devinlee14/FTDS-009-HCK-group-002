"""
// function.py //
This programme was created to store the function used through out this project.
"""


import re
from nltk.tokenize import word_tokenize

# Create A Function for Text Preprocessing
def text_preprocessing(text, lemmatizer, sw):
  # Case folding
  text = text.lower()

  # Mention removal
  text = re.sub("@[A-Za-z0-9_]+", " ", text)

  # Hashtags removal
  text = re.sub("#[A-Za-z0-9_]+", " ", text)

  # Newline removal (\n)
  text = re.sub(r"\\n", " ",text)

  # Whitespace removal
  text = text.strip()

  # URL removal
  text = re.sub(r"http\S+", " ", text)
  text = re.sub(r"www.\S+", " ", text)

  # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
  text = re.sub("[^A-Za-z\s']", " ", text)

  # Tokenization
  tokens = word_tokenize(text)
  
  # Stopwords removal
  tokens = [word for word in tokens if word not in sw]
  
  # Lemmatization
  tokens = [lemmatizer.lemmatize(word) for word in tokens]
  
  # Combining Tokens
  text = ' '.join(tokens)
  
  return text
