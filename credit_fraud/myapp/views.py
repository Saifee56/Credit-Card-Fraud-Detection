from django.shortcuts import render, redirect
from django.http import HttpResponse
from joblib import load


model=load(r'C:\Users\i-saifee\Desktop\Credit_card_fraud\Credit-Card-Fraud-Detection\credit_fraud/model.joblib')


def form1(request):
    return render(request,'form1.html')

# #Form information
def form_info(request):
    merchant=request.GET['merchant']
    category=request.get['category']
    gender=request.GET['gender']
    job=request.GET['job']
    unix_time=request.GET['unix_time']
    merch_lat=request.GET['merch_lat']
    merch_long=request.GET['merch_long']

    y_pred=model.predict([[merchant,category,gender,job,unix_time,merch_lat,merch_long]])

    if y_pred[0] >0.5:
        y_pred='The user is attempting fraud'
    elif y_pred[0] <0.5:
        y_pred='The user is pure'
    
    return render(request,result.html,{'result':y_pred})
     