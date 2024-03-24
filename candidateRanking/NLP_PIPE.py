import nltk
import re,string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('popular')

#Clean text, tokenization, remove stop words and stemming

class NLP_SERVICE:

    def __init__(self,doc:str) -> None:
        self.ps = PorterStemmer()
        self.doc = doc


    def clean_text(self):
        text = self.doc.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        self.doc = text
        return self
    
    def transform_text(self):
        text = word_tokenize(self.doc)
        words = [self.ps.stem(w) for w in text if w not in set(stopwords.words('english'))]
        self.doc = " ".join(words)
        return self

    def get_doc(self):
        return self.doc