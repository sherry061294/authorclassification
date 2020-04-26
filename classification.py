import pandas
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# number  of sentences - done
# Average number of words per sentence in the file - done
# Average word length in the file - done
# Number of stop words per book - done
# Number of determiners per book
# Number of possessives per book 


def get_no_of_sentences_in_file(filename):
    # folder = nltk.data.find(filename)
    corpusReader = nltk.corpus.PlaintextCorpusReader(filename,'.txt')
    print(corpusReader)
    num_sentences = len(corpusReader.sents())
    # print ('The number of patagraphs =', len(corpusReader.paras()))
    num_words = len([word for sentence in corpusReader.sents() for word in sentence])
    num_chars = len([char for sentence in corpusReader.sents() for word in sentence for char in word])
    print ("The number of characters =", num_chars)
    print ('The number of words =', num_words)
    print ('The number of sentences =', num_sentences)

    return [num_sentences,num_words,num_chars]
#START
authorName = []
number_of_sentences_file = []
avg_no_word_in_sentence_file = []
avg_word_length_file = []
avg_no_of_stopwords = []
#Read one File
import os
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
        no_of_stopwords = []
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
            num_chars.append(word_len)
            stopWords = set(stopwords.words('english'))
            

            for w in word_tokens:
                if w in stopWords:
                    no_of_stopwords.append(w)
        
        avg_no_of_stopwords.append(len(no_of_stopwords)/num_sentences)
        print("avg_no_of_stopwords - ",avg_no_of_stopwords)
        # print(num_chars)  
        print(sum(num_words_sentence))
        print(sum(num_chars))
        avg_no_word_in_sentence_file.append(sum(num_words_sentence)/num_sentences)
        avg_word_length_file.append(sum(num_chars)/sum(num_words_sentence))
        print("number_of_sentences_file - ",number_of_sentences_file)
        print("avg_no_word_in_sentence_file - ",avg_no_word_in_sentence_file)
        print("avg_word_length_file - ",avg_word_length_file)
        print()
        

        
        



        # [num_sentences,num_words,num_chars] = get_no_of_sentences_in_file(filename_full_path)
        # number_of_sentences_file.append(num_sentences)
        # avg_no_word_in_sentence_file.append(num_words/num_sentences)
        # avg_word_len_file.append(num_chars/num_words)

        
        
         
# Get all information/ features from that file. including author name

# append each to their own lists

#Take next file / Repeat from START till all files are over

# Add all lists as colums to the data frame

#Do Train/Test Split

#Do ML Model 

#Print results

#Profit