import csv
import os
from .models import TemporaryFiles
from credit_fraud import settings as s
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def file_reader(model):
    
    encoder=LabelEncoder()
    get_file_from_model=TemporaryFiles.objects.filter().first()

    file=open(file=get_file_from_model.file.path)
    df=pd.read_csv(file)

    df2=df[['merchant','category','gender','job','unix_time','merch_lat','merch_long']]

    # model prediction
    df['merchant']=encoder.fit_transform(df['merchant'])
    df['category']=encoder.fit_transform(df['category'])
    df['job']=encoder.fit_transform(df['job'])
    df['gender']=encoder.fit_transform(df['gender'])

    y_pred=model.predict(df[['merchant','category','gender','job','unix_time','merch_lat','merch_long']])

    df2['prediction']=y_pred
    return df2
