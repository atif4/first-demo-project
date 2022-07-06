import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def get_lemmatization(input_str_name):
    input_str =input_str_name 
    for i in input_str:
        a = nltk.word_tokenize(i)
        for word in a:
            print(lemmatizer.lemmatize(word))