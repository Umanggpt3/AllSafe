from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize

import pickle
import pandas as pd
import json
# Create your views here.

@csrf_exempt
def test(request):
    print(request.is_ajax())
    print(request)
    json_text = json.loads(request.body)
    body_text = json_text["body_text"].split("\n")

    body_html  = json_text["body_html"]
    for e in body_text:
        if(classify(e)[0]):
            print("{} --> {}".format(e,classify(e)[0]))
            body_html.replace(e,"")
    return HttpResponse(body_html)

def classify(txt):
    mnb=pickle.load(open('../ML_Models/saved_classifiers/mnb.pickle','rb'))
    vect=pickle.load(open('../ML_Models/saved_classifiers/vectorizer.pickle','rb'))
    offensive_list=(pd.read_csv("../Datasets/Offensive_word_list.txt")).values.flatten()
    cd=cleanData(txt)
    # for w in offensive_list:
    #     if w in cd.split(' '):
    #         print(w)
    pred=mnb.predict(vect.transform([cd]))
    return pred

def cleanData(txt):
    w_list=word_tokenize(txt)
    ps=PorterStemmer()
    cleaned=[]
    for w in w_list:
        cleaned.append(ps.stem(w.lower()))
    return ' '.join(cleaned)
