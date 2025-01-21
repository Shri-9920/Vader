#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyMuPDF pillow pytesseract


# In[1]:


pip install nltk


# In[1]:


from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment of a text
text = "This product is absolutely amazing! I love it!!! 😊"
scores = sia.polarity_scores(text)

# Print the scores
print("Positive:", scores['pos'])
print("Neutral:", scores['neu'])
print("Negative:", scores['neg'])
print("Compound Score:", scores['compound'])


# In[2]:


pip install --upgrade nltk


# In[3]:


import nltk
nltk.download('vader_lexicon')


# In[5]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment of a text
text = "This product is absolutely amazing! I love it!!! 😊"
scores = sia.polarity_scores(text)

# Print the scores
print("Positive:", scores['pos'])
print("Neutral:", scores['neu'])
print("Negative:", scores['neg'])
print("Compound Score:", scores['compound'])


# In[6]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment of a text
text = "This product is absolutely terrible! I hate it!!! 😊"
scores = sia.polarity_scores(text)

# Print the scores
print("Positive:", scores['pos'])
print("Neutral:", scores['neu'])
print("Negative:", scores['neg'])
print("Compound Score:", scores['compound'])


# In[7]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment of a text
text = "This product is absolutely  I  it!!! 😊"
scores = sia.polarity_scores(text)

# Print the scores
print("Positive:", scores['pos'])
print("Neutral:", scores['neu'])
print("Negative:", scores['neg'])
print("Compound Score:", scores['compound'])


# In[ ]:




