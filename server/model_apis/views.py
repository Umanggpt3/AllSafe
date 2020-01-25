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
import re
# Create your views here.

@csrf_exempt
def test(request):
    flag=(json.loads(request.body))["flag"]
    body_html  = (json.loads(request.body))["body_html"]
    print("bully content moderation")
    offensive_list=(pd.read_csv("../Datasets/Offensive_word_list_all.csv",sep='\n')).values.flatten()
    mnb=pickle.load(open('../ML_Models/alt_model.pickle','rb'))
    vect=pickle.load(open('../ML_Models/vectorizer.pickle','rb'))
    b_text=BeautifulSoup(body_html,"lxml").get_text() 
    txt_list=sent_tokenize(b_text)
    count=0
    print(flag)
    if flag == 1:
        print("classifier chal rha hai")
        for s in txt_list:
            #print("{} --> {}".format(s,classify(s,mnb,vect)))
            if classify(s,mnb,vect)[0]!='False':
                count=count+1
                body_html=body_html.replace(s,"")        
    for w in word_tokenize(body_html):
        if w.lower() in offensive_list:
            pattern=re.compile(r"([^A-Za-z<>]){}([^A-Za-z<>])".format(w))
            body_html=re.sub(pattern, " * ",body_html)
    body_html=body_html.replace("<script","<script async ")
    print("returning")
    return HttpResponse(body_html)    

# @csrf_exempt
# def test(request):
#     body_html  = (json.loads(request.body))["body_html"]
#     print("only content moderation")
#     offensive_list=(pd.read_csv("../Datasets/Offensive_word_list_en.csv")).values.flatten()
#     b_text=BeautifulSoup(body_html,"lxml").get_text() 
#     txt_list=sent_tokenize(b_text)
#     count=0
#     for w in word_tokenize(body_html):
#         if w.lower() in offensive_list:
#             pattern=re.compile(r"([^A-Za-z<>]){}([^A-Za-z<>])".format(w))
#             body_html=re.sub(pattern, str("*"*len(w)),body_html)
#     body_html=body_html.replace("<script","<script async ")
#     return HttpResponse(body_html)    

def classify(txt,mnb,vect):
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
