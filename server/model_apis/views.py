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
    print(json_text)
    # print(request.method)
    # texts = json.loads(json_text)['body_text']
    # print(json_text["body_text"])
    print(classify("You are sso dumb, fool"))
    return HttpResponse("Request Recieved!")

def classify(txt):
    mnb=pickle.load(open('../ML_Models/saved_classifiers/mnb.pickle','rb'))
    vect=pickle.load(open('../ML_Models/saved_classifiers/vectorizer.pickle','rb'))
    offensive_list=(pd.read_csv("../Datasets/Offensive_word_list.txt")).values.flatten()
    cd=cleanData(txt)
    for w in offensive_list:
        if w in cd:
            print(w)
    pred=mnb.predict(vect.transform([cd]))
    return pred

def cleanData(txt):
    w_list=word_tokenize(txt)
    ps=PorterStemmer()
    cleaned=[]
    for w in w_list:
        cleaned.append(ps.stem(w.lower()))
    return ' '.join(cleaned)
