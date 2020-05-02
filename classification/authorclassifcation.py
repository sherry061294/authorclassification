import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import nltk 
import os
import string

import spacy 
nlp = spacy.load('en', disable=['parser', 'ner'])
nlp.max_length = 5000000
sent = "The striped bats are hanging on their feet for best"
text = []
authorName =[]
stopWords = set(stopwords.words('english'))
count=0
for filename in os.listdir(os.getcwd() + '/final/data/raw_data/'):
    filename_full_path = os.getcwd() + '/final/data/raw_data/'+ filename
    print(filename)
    with open(filename_full_path, 'r') as f:
        authorName.append(filename.split('_')[0])
        filedata = f.read()
        
        # Lower case
        filedata_lower = filedata.lower()
        
        # Punctuation Removal
        filedata_no_punct = filedata_lower.translate(str.maketrans('', '', string.punctuation))
        doc = nlp(filedata_no_punct)

        # Extract the lemma for each token and join
        filedata_lemmatized = " ".join([token.lemma_ for token in doc])
        # print(filedata_lemmatized)
        
        #Stopword removal
        word_tokens = word_tokenize(filedata_lemmatized) 
        filedata_no_stop = [w for w in word_tokens if not w in stopWords] 

        filedata_final = " ".join([word for word in filedata_no_stop])
        text.append(filedata_final)
        count+=1
        print(count)
dfObj = pd.DataFrame(columns=[])

dfObj['text'] = text
dfObj['author_name'] = authorName

print(dfObj)