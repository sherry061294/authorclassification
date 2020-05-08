import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import nltk 
import os
import string
import spacy 

nlp = spacy.load('en', disable=['parser', 'ner'])
nlp.max_length = 5000000
text = []
authorName =[]
stopWords = set(stopwords.words('english'))
count=0

def pre_process_func(filedata):
    # Lower case
    filedata_lower = filedata.lower()
    
    # Punctuation Removal
    filedata_no_punct = filedata_lower.translate(str.maketrans('', '', string.punctuation))

    # Extract the lemma for each token and join
    doc = nlp(filedata_no_punct)
    filedata_lemmatized = " ".join([token.lemma_ for token in doc])
    # print(filedata_lemmatized)
    
    #Stopword removal
    word_tokens = word_tokenize(filedata_lemmatized) 
    filedata_no_stop = [w for w in word_tokens if not w in stopWords] 
    filedata_final = " ".join([word for word in filedata_no_stop])
    
    return filedata_final

#Pre-Processing
for filename in os.listdir(os.getcwd() + '/../data/raw_data/'):
    filename_full_path = os.getcwd() + '/../data/raw_data/'+ filename
    print(filename)
    with open(filename_full_path, 'r') as f:
        authorName.append(filename.split('_')[0])
        filedata = f.read()
        filedata_final = pre_process_func(filedata)
        text.append(filedata_final)
        count+=1
        print(count)
dfObj = pd.DataFrame(columns=[])

dfObj['text'] = text
dfObj['author_name'] = authorName

print(dfObj)

X = dfObj['text']
y1 = dfObj['author_name']
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y1)
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.1, random_state=1234)

bow_transformer=CountVectorizer().fit(X_train)

text_bow_train=bow_transformer.transform(X_train)

text_bow_test=bow_transformer.transform(X_test)


# Importing necessary libraries
from sklearn.naive_bayes import MultinomialNB
# instantiating the model with Multinomial Naive Bayes..
model = MultinomialNB()
# training the model...
model = model.fit(text_bow_train, y_train)

model.score(text_bow_train, y_train)
                                  
print(model.score(text_bow_test, y_test))
predictions = model.predict(text_bow_test)
print(classification_report(y_test,predictions))


twogram_text = []
twogram_label = []

for filename in os.listdir(os.getcwd() + '/../data/generated_data/2gram'):
    filename_full_path = os.getcwd() + '/../data/generated_data/2gram/'+ filename
    if filename.startswith('perp_'):
        continue
    with open(filename_full_path, 'r') as f:
        twogram_label.append(filename.split('_')[0].replace("_"," "))
        filedata = f.read()
        filedata_without_start_tag = filedata.replace("<s>","")
        filedata_without_start_end_tag = filedata_without_start_tag.replace(" </s>\n",".")
        filedata_final = pre_process_func(filedata_without_start_end_tag)
        twogram_text.append(filedata_final)
print(twogram_label)
encoded_2gram_labels = labelencoder.fit_transform(twogram_label)
twongram_bow = bow_transformer.transform(twogram_text)

# for i in range(10):
#     print("Original " + str(y1[i]) + "  " + str(y[i]) + "\n")
#     print("second one "+ str(encoded_2gram_labels[i]) + " " +  str(twogram_label[i]) + "\n")


print("\t \t \t Scores for bigrams")
predictions = model.predict(twongram_bow)
print(classification_report(encoded_2gram_labels,predictions))


trigram_text = []
trigram_label = []

for filename in os.listdir(os.getcwd() + '/../data/generated_data/3gram'):
    filename_full_path = os.getcwd() + '/../data/generated_data/3gram/'+ filename
    if filename.startswith('perp_'):
        continue
    with open(filename_full_path, 'r') as f:
        trigram_label.append(filename.split('_')[0].replace("_"," "))
        filedata = f.read()
        filedata_without_start_tag = filedata.replace("<s>","")
        filedata_without_start_end_tag = filedata_without_start_tag.replace(" </s>\n",".")
        filedata_final = pre_process_func(filedata_without_start_end_tag)
        trigram_text.append(filedata_final)

encoded_3gram_labels = labelencoder.fit_transform(trigram_label)
tringram_bow = bow_transformer.transform(trigram_text)


print("\t \t \t Scores for trigrams")
predictions = model.predict(tringram_bow)
print(classification_report(encoded_3gram_labels,predictions))

quadgram_text = []
quadgram_label = []

for filename in os.listdir(os.getcwd() + '/../data/generated_data/4gram'):
    filename_full_path = os.getcwd() + '/../data/generated_data/4gram/'+ filename
    if filename.startswith('perp_'):
        continue
    with open(filename_full_path, 'r') as f:
        quadgram_label.append(filename.split('_')[0].replace("_"," "))
        filedata = f.read()
        filedata_without_start_tag = filedata.replace("<s>","")
        filedata_without_start_end_tag = filedata_without_start_tag.replace(" </s>\n",".")
        filedata_final = pre_process_func(filedata_without_start_end_tag)
        quadgram_text.append(filedata_final)

encoded_4gram_labels = labelencoder.fit_transform(quadgram_label)
quadngram_bow = bow_transformer.transform(quadgram_text)


print("\t \t \t Scores for quadgrams")
predictions = model.predict(quadngram_bow)
print(classification_report(encoded_4gram_labels,predictions))

