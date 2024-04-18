from django.shortcuts import render, redirect
from django.http import HttpResponse
from joblib import load
# from .forms import UploadFileForm
import pandas as pd
from joblib import load
import csv
import myapp.csv_handler as ch
from .models import TemporaryFiles
import csv
from io import StringIO
from django.http import HttpResponse


model=load(r"C:\Users\my pc\Desktop\Credit_card_fraud\Credit-Card-Fraud-Detection\model\credit_model.joblib")


def form1(request):
    if request.method=="POST":
        
        csv_file=request.FILES.get('csv_file')

        new_file=TemporaryFiles.objects.create(file=csv_file)
        new_file.save()

        dataframe=ch.file_reader(model=model)
        return download_dataframe_as_csv(request=request,dataframe=dataframe)

    return render(request,'form1.html')

# #Form information
def form_info(request):
    return render(request,"result.html")

    
    

def download_dataframe_as_csv(request, dataframe, filename="prediction_data.csv"):

  # Create a StringIO object to hold the CSV data in memory
  csv_buffer = StringIO()
  writer = csv.writer(csv_buffer)

  # Write the column headers
  writer.writerow(dataframe.columns.tolist())

  # Write the data rows
  for index, row in dataframe.iterrows():
    writer.writerow(row.to_list())

  # Set the HTTP response headers
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = f'attachment; filename={filename}'

  # Write the CSV data to the response
  response.write(csv_buffer.getvalue().encode('utf-8'))

  return response