from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
import pickle
import pandas as pd
import json
# Create your views here.

@csrf_exempt
def test(request):
    # print(request.is_ajax())
    # print(request)
    json_text = json.loads(request.body)
    body_html  = json_text["body_html"]
    cens_txt=word_tokenize(json_text["body_text"])
    offensive_list=(pd.read_csv("../Datasets/Offensive_word_list.txt")).values.flatten()
    for i in range(len(cens_txt)):
        if cens_txt[i] in offensive_list:
            #print(cens_txt[i])
            cens_txt[i]="*"*len(cens_txt[i])
    body_text = sent_tokenize(' '.join(cens_txt))
    for e in body_text:
        if(classify(e)[0]):
            #print("{} --> {}".format(e,classify(e)[0]))
            body_text.replace(e,"")
    return HttpResponse(body_text)

def classify(txt):
    mnb=pickle.load(open('../ML_Models/alt_model.pickle','rb'))
    vect=pickle.load(open('../ML_Models/vectorizer.pickle','rb'))
    cd=cleanData(txt)
    pred=mnb.predict(vect.transform([cd]))
    return pred

def cleanData(txt):
    w_list=word_tokenize(txt)
    ps=PorterStemmer()
    cleaned=[]
    for w in w_list:
        cleaned.append(ps.stem(w.lower()))
    return ' '.join(cleaned)
