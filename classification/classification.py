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
for filename in os.listdir(os.getcwd() + '/final/data/processed_data/'):
    filename_full_path = os.getcwd() + '/final/data/processed_data/'+ filename
    print(filename)
    with open(filename_full_path, 'r') as f:
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

import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(dfObj, dfObj2, test_size=0.1, random_state=0)
# print(dfObj)
# print(dfObj2)
# print(X_train)
# print(y_train)
# print(X_test)
# print(y_test)
# columns = X_train.columns
# os_data_X,os_data_y=os.fit_sample(X_train, y_train)
# os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
# os_data_y= pd.DataFrame(data=os_data_y,columns=['author_name'])

# print("length of oversampled data is ",len(os_data_X))
# print("Number of no subscription in oversampled data",len(os_data_y[os_data_y['author_name']==0]))
# print("Number of subscription",len(os_data_y[os_data_y['author_name']==1]))
# print("Proportion of no subscription data in oversampled data is ",len(os_data_y[os_data_y['author_name']==0])/len(os_data_X))
# print("Proportion of subscription data in oversampled data is ",len(os_data_y[os_data_y['author_name']==1])/len(os_data_X))

# logreg = LogisticRegression()
# logreg.fit(X_train, y_train)

# y_pred = logreg.predict(X_test)
# print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

# Importing necessary libraries
from sklearn.naive_bayes import MultinomialNB
# instantiating the model with Multinomial Naive Bayes..
model = MultinomialNB()
# training the model...
model = model.fit(X_train, y_train)

model.score(X_train, y_train)
print("Accuracy")
print(model.score(X_test, y_test))

from sklearn.metrics import classification_report
 
# getting the predictions of the Validation Set...
predictions = model.predict(X_test)
# getting the Precision, Recall, F1-Score
print(classification_report(y_test,predictions))