from django.shortcuts import render, redirect
from django.http import HttpResponse

def form1(request):
    return render(request,'form1.html')

#Form information
def info(request):
    transactionId = request.get('transactionId')
    customerID = request.get('customerID')
    terminalID = request.get('terminalID')
    datetime = request.get('datetime')
    transactionAmount = request.get('transactionAmount')
    return render(request, 'details.html', {'details':{transactionId,transactionAmount,terminalID,customerID,datetime}})
