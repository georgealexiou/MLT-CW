import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

SYMBOLS_TO_REMOVE = re.compile('[/(){}\[\]\|@,.;¿`\'"+><$%^*]')
BAD_SYMBOLS = re.compile('[^0-9a-z +_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text_block(text):
    text = text.lower()

    text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    return text