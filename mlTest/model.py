import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk
import enchant
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import pickle


#TODO run time 1
#nltk.download("stopwords")
#nltk.download("punkt")
#nltk.download("wordnet")
nltk.download("omw-1.4")

def checkSuicide(data):
    spell_dict = enchant.Dict('en-US')


    test = pd.DataFrame({"id":[42],"category":[0],"tweet":[data]})


   # test = pd.read_csv('test.tsv', header=0, delimiter="\t", \
    #               quoting=3 )


    with open("mlTest/vector","rb") as f:
        vectorizer = pickle.load(f)

    stop_words = set(stopwords.words("english"))
    clean_test_tweets = []
    for i in range(0, len(test["tweet"])):
        sent = test["tweet"][i]
        sent = sent.lower()
        sen = re.sub("[^a-zA-Z]", " ", sent)
        if len(sen) > 0:
            clean = []
            word = word_tokenize(sen)
            for w in word:
                if not w in stop_words and len(w) > 2:
                    if wordnet.synsets(w) and spell_dict.check(w):
                        clean.append(w)
            clean_test_tweets.append(" ".join(clean))

    test_data_features = vectorizer.transform(clean_test_tweets)
    np.asarray(test_data_features)

    with open("mlTest/model", "rb") as f:
        classifier = pickle.load(f)

    result = classifier.predict(test_data_features)

    data = {'id': test['id'], 'Category': result}
    output = pd.DataFrame(data)


    return output


print(checkSuicide(" I suicide myself"))
