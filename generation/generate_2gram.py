import numpy as np
import os

def generate_sentence(word_probs, max_words):
    '''
    Generates a sentence based on word counts
    '''
    p1_word = "<s>"
    sentence = "<s> "

    for i in range(max_words):
        word_prob = word_probs[p1_word]
        next_word = np.random.choice(
            [word for word in word_prob], # list of words to choose from
            1, # number of words to choose
            [prob for _, prob in word_prob.items()])[0] # weights

        # stop generation if we've hit the end sentence tag
        if next_word == "</s>":
            break

        # add word to sentence and reset previous words
        sentence += next_word + " "
        p1_word = next_word

    return sentence + "</s>"


if __name__ == "__main__":
    directory = "%s/../data/processed_data" % os.getcwd()

    # for each author
    for filename in os.listdir(directory):
        # initialize dictionary with sentence begin tag
        word_probs = dict()
        word_probs["<s>"] = dict()

        # read through authors sentences
        with open(os.path.join(directory, filename), "r") as ifile:

            # iterate through file and update word counts
            for line in ifile:
                sentence = line[:-1].split(" ") # skip the trailing newline character

                # initialize sentence tag
                p1_word = "<s>"

                for word in sentence[1:]:
                    # initialize empty dictionaries for new words
                    if p1_word not in word_probs:
                        word_probs[p1_word] = dict()

                    # if we have not seen this word combination, initialize count to 1
                    if word not in word_probs[p1_word]:
                        word_probs[p1_word][word] = 1
                    else:
                        word_probs[p1_word][word] += 1 # increment the count of this 2-word run

                    # reset previous words
                    p1_word = word

        # normalize counts
        for p1_word in word_probs:
            tot = sum(word_probs[p1_word].values())
            for word in word_probs[p1_word]:
              word_probs[p1_word][word] = word_probs[p1_word][word] / tot

        # generate sentences
        num_sentences = 100
        max_length = 30
        with open("%s/../data/generated_data/2gram/%s" % (os.getcwd(), filename), "w") as ofile:
            for _ in range(num_sentences):
                sentence =  generate_sentence(word_probs, max_length)
                ofile.write(sentence + "\n")
