from collections import Counter
import os
import re

def process_text(line):
	line = line.replace("\n", " ") # remove newline
	line = line.replace("Mrs.", "Mrs") # remove expected periods
	line = line.replace("Mr.", "Mr")
	line = line.replace("etc.", "etc")
	line = line.replace("P.S.", "PS")

	return line


if __name__ == "__main__":
	raw_data_path = "%s/../data/raw_data" % os.getcwd()

	author_text = {}

	for file_name in os.listdir(raw_data_path):
		print(file_name)
		author = "_".join(file_name.split("__")[0].split())

		# If we haven't seen this author, add an empty list to the dictionary
		if author not in author_text:
			author_text[author] = []

		# Process the text of one of the books
		full_text = open(os.path.join(raw_data_path, file_name), "r").read()

		full_text = process_text(full_text)

		# For each sentence, find each word, add start/end sentence tags, and add to full list of author text
		for sentence in re.split("\. |\? |\! ", full_text):
			arr = [" ".join(re.findall("[a-zA-Z]+'?[a-zA-Z]+", word)).lower() for word in sentence.split()]

			sentence = " ".join(arr)
			sentence = "<s> " + sentence + " </s>"
			sentence = re.sub("\s+", " ", sentence) # replace any whitespace with a single space

			author_text[author].append(sentence)

	# Write out evey sentence for each author to their own file
	for author in author_text:
		with open("%s/../data/processed_data/%s.txt" % (os.getcwd(), author), "w") as ofile:
			for sentence in author_text[author]:
				ofile.write(sentence + "\n")
