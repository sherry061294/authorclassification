import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# number  of sentences - done
# Average number of words per sentence in the file - done
# Average word length in the file - done
# Number of stop words per book - done
# Number of determiners per book -done
# Number of possessives per book - done


#START
authorName = []
number_of_sentences_file = []
avg_no_word_in_sentence_file = []
avg_word_length_file = []
avg_no_of_stopwords = []
avg_no_of_determiners = []
avg_no_of_possessives = []
#Read one File
import os
stopWords = set(stopwords.words('english'))

with open(os.getcwd() +'/DeterminersList', 'r') as d :
    Determiners_list = d.read()
d.close()
with open (os.getcwd() +'/PossessivesList', 'r') as p:
    Possessives_list = p.read()
p.close()
count=0
path = os.getcwd() + '/../data/processed_data_feature_engineering/'
print(path)
for filename in os.listdir(path):
    filename_full_path = path + filename
    print(filename)
    with open(filename_full_path, 'r') as f:
        print(count)
        authorName.append(filename.split('_')[0])
        filedata = f.read()
        num_sentences = len(filedata.split('\n'))
        number_of_sentences_file.append(num_sentences - 1)
        num_words_sentence = []
        num_chars = []
        no_of_determiners = no_of_possessives = 0
        no_of_stopwords = 0
        for sentence in filedata.split('\n'):
            word_tokens = sentence.split()
            # print(word_tokens)
            num_words_sentence.append(len(word_tokens)-2)
            word_len = 0
            for word in word_tokens:
                if word == '<s>' or word == '</s>':
                    continue
                else:
                    word_len += len(word)
            
                if word in stopWords:
                    no_of_stopwords+=1

                if word in Determiners_list:
                    no_of_determiners += 1
                if word in Possessives_list:
                    no_of_possessives += 1
            num_chars.append(word_len)
        
        avg_no_of_stopwords.append(no_of_stopwords/num_sentences)
        avg_no_of_determiners.append(no_of_determiners/num_sentences)
        avg_no_of_possessives.append(no_of_possessives/num_sentences)
        # print("avg_no_of_stopwords - ",avg_no_of_stopwords)
        # # print(num_chars)  
        # print("number of words in a sentence - ",sum(num_words_sentence))
        # print("number of chars - ",sum(num_chars))
        avg_no_word_in_sentence_file.append(sum(num_words_sentence)/num_sentences)
        avg_word_length_file.append(sum(num_chars)/sum(num_words_sentence))
        # print("number_of_sentences_file - ",number_of_sentences_file)
        # print("avg_no_word_in_sentence_file - ",avg_no_word_in_sentence_file)
        # print("avg_word_length_file - ",avg_word_length_file)
        count+=1
        print(count)
        print()

# Add all lists as colums to the data frame

dfObj = pd.DataFrame(columns=[])
dfObj2 = pd.DataFrame(columns=[])
dfObj['avg_stopwords'] = avg_no_of_stopwords
dfObj['avg_determiners'] = avg_no_of_determiners
dfObj['avg_possessives'] = avg_no_of_possessives
dfObj['avg_word_sentence'] = avg_no_word_in_sentence_file
dfObj['avg_word_length'] = avg_word_length_file
dfObj['no_of_sentences'] = number_of_sentences_file

dfObj2['author_name'] = authorName
print(dfObj)

print(dfObj2)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(dfObj, dfObj2, test_size=0.1, random_state=0)

model = MultinomialNB()
# training the model...
model = model.fit(X_train, y_train)

# getting the predictions of the Validation Set...
predictions = model.predict(X_test)
# getting the Precision, Recall, F1-Score
print(classification_report(y_test,predictions))