from django.shortcuts import render
import pandas as pd
import json
from django.conf import settings
import os

def table(request):
    
    #df = pd.read_excel(r"" + settings.BASE_DIR + "static\\overall_ranking\\excel\\Overall Rank.xlsx")
    df = pd.read_excel(settings.STATICFILES_DIRS_EXCEL)
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)

 
    context = {'d': data}

    

    return render(request, 'overall_ranking/ranking_list.html',context)

     

