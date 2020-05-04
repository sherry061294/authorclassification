import numpy as np
import os

def perplexity(word_probs, sentence):
    sentence = sentence.split(" ")
    sentence_prob = 1

    for i in range(len(sentence) - 2):
        word_1 = sentence[i]
        word_2 = sentence[i + 1]
        word_3 = sentence[i + 2]
        try:
            word_prob = word_probs[word_1][word_2][word_3] # probability of current word triplet
        except:
            word_prob = 1 # if the sentence got cut off at max_len, this probability will not be found - just set to 1
        sentence_prob *= word_prob # update sentence probability

    perplexity = 1 / (pow(sentence_prob, 1.0 / len(sentence)))

    return perplexity

def generate_sentence(word_probs, max_words):
    '''
    Generates a sentence based on word counts
    '''
    p2_word = "<s>"
    p1_word = "<s>"
    sentence = p2_word + " " + p1_word + " "

    for i in range(max_words):
        word_prob = word_probs[p2_word][p1_word]
        next_word = np.random.choice(
            [word for word in word_prob], # list of words to choose from
            1, # number of words to choose
            [prob for _, prob in word_prob.items()])[0] # weights

        # stop generation if we've hit the end sentence tag
        if next_word == "</s>":
            break

        # add word to sentence and reset previous words
        sentence += next_word + " "
        p2_word = p1_word
        p1_word = next_word

    sentence = sentence + "</s>"

    perp = perplexity(word_probs, sentence)

    return sentence, perp


if __name__ == "__main__":
    directory = "%s/../data/processed_data" % os.getcwd()

    # for each author
    for filename in os.listdir(directory):
        # initialize dictionary with sentence begin tags
        word_probs = dict()
        word_probs["<s>"] = dict()
        word_probs["<s>"]["<s>"] = dict()

        # read through authors sentences
        with open(os.path.join(directory, filename), "r") as ifile:

            # iterate through file and update counts
            for line in ifile:
                sentence = line[:-1].split(" ") # skip the trailing newline character

                # initialize sentence tags
                p2_word = "<s>"
                p1_word = "<s>"

                for word in sentence[1:]:
                    # initialize empty dictionaries for new words
                    if p2_word not in word_probs:
                        word_probs[p2_word] = dict()
                    if p1_word not in word_probs[p2_word]:
                        word_probs[p2_word][p1_word] = dict()

                    # if we have not seen this word combination, initialize count to 1
                    if word not in word_probs[p2_word][p1_word]:
                        word_probs[p2_word][p1_word][word] = 1
                    else:
                        word_probs[p2_word][p1_word][word] += 1 # increment the count of this 3-word run

                    # reset previous words
                    p2_word = p1_word
                    p1_word = word

        # normalize counts
        for p2_word in word_probs:
            for p1_word in word_probs[p2_word]:
                tot = sum(word_probs[p2_word][p1_word].values())
                for word in word_probs[p2_word][p1_word]:
                  word_probs[p2_word][p1_word][word] = word_probs[p2_word][p1_word][word] / tot

        # generate sentences
        num_sentences = 100
        max_length = 50
        sent_file = open("%s/../data/generated_data/3gram/%s" % (os.getcwd(), filename), "w")
        perp_file = open("%s/../data/generated_data/3gram/perp_%s" % (os.getcwd(), filename), "w")
        for _ in range(num_sentences):
            sentence, perp = generate_sentence(word_probs, max_length)
            sent_file.write(sentence + "\n")
            perp_file.write(str(perp) + "\n")
