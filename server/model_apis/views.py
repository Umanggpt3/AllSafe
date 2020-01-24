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
from bs4 import BeautifulSoup
# Create your views here.

@csrf_exempt
def test(request):
    offensive_list=(pd.read_csv("../Datasets/Offensive_word_list.txt")).values.flatten()
    mnb=pickle.load(open('../ML_Models/alt_model.pickle','rb'))
    vect=pickle.load(open('../ML_Models/vectorizer.pickle','rb'))
    body_html  = (json.loads(request.body))["body_html"]
    b_text=BeautifulSoup(body_html).get_text() 
    txt_list=sent_tokenize(b_text)
    for s in txt_list:
        if classify(s,mnb,vect):
            body_html=body_html.replace(s,"")
    for w in word_tokenize(body_html):
        if w.lower() in offensive_list:
            if w=='class':
                continue
            body_html=body_html.replace((" "+w+" "),str("*"*len(w)))
    
    #print(body_html)
    body_html=body_html.replace("<script","<script async ")
    return HttpResponse(body_html)    

def classify(txt,mnb,vect):
    cd=cleanData(txt)
    pred=mnb.predict(vect.transform([cd]))
    return pred[0]

def cleanData(txt):
    w_list=word_tokenize(txt)
    ps=PorterStemmer()
    cleaned=[]
    for w in w_list:
        cleaned.append(ps.stem(w.lower()))
    return ' '.join(cleaned)
