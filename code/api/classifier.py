import pandas as pd
import numpy as np
import pickle
from unidecode import unidecode
import re
import nltk
from bs4 import BeautifulSoup
from config import *


class Classifier:

    def __init__(self):

        self.model = pickle.load(open(PATH_TO_MODEL, 'rb'))

    def clean_text(self, text):
        REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
        BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
        STOPWORDS = set(nltk.corpus.stopwords.words('english'))

        text = str(text)

        text = unidecode(text)
        text = BeautifulSoup(text, "html.parser").text  # HTML decoding
        text = text.lower()  # lowercase text
        # replace REPLACE_BY_SPACE_RE symbols by space in text
        text = REPLACE_BY_SPACE_RE.sub(' ', text)
        # delete symbols which are in BAD_SYMBOLS_RE from text
        text = BAD_SYMBOLS_RE.sub('', text)
        # delete stopwors from text
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        return text

    def predict(self, synopsis):

        categories = []

        text = synopsis

        text = text.strip()

        text = self.clean_text(text)

        for tag, model in self.model.items():

            pred = model.predict([text])[0]

            if pred == 1:

                categories.append(tag)

        return {'categories': categories}
