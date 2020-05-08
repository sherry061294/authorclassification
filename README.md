# AUTHOR CLASSIFICATION AND TEXT GENERATION

This project has two main tasks. **Author classification** and **Text Generation**.
The Data Set used is taken from the project Gutenburg collection. We make use of a small subset of it, about 331 books taken from 11 authors.

# Text Generation

The scripts for this task are present in the generation folder. The text eneration task makes use of the following files:

  - `generate_2gram.py` : This file is responsible for generating bigram text. It can be run directly using python 3 from the command line. It makes use of the data stored in the `data/processed_data` folder. The generated text can be found in the `data/generated_data` folder. The data here is used as input in the `authorclassification.py` file. 
  - `generate_3gram` and `generate_4gram` files can be used to generate trigram and quadgram data respectively.
  ```sh
$ cd generation
$ python3 generate_2gram.py
$ python3 generate_3gram.py
$ python3 generate_4gram.py
```

# Author Classification

The scripts for this task are present in the classification folder. The author classification task makes use of the following files:

  - `classification.py` : This file is responsible for the baseline model. It can be run directly using `python 3` from the command line. It makes use of the data stored in the `data/processed_data_feature_engineering` folder. This file also requires the `determinersList` and `possessivesList` to be present on the same level in the folder structure as the running program.
  ```sh
$ cd classification
$ python3 classifcation.py
```
  - `authorclassification.py` : This file is resposible for the bag of words model. It can be run directly from the command line using `python 3`. It makes use of the data stored in the `data/raw_data folder`. Other data used by this file is the data generated from the text generation algorithm (the 2gram, 3gram and 4gram data in the `data/generated_data folder`)
  ```sh
$ cd classification
$ python3 authorclassifcation.py
```
