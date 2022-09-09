from django.shortcuts import render
from django.http import HttpResponse, JsonResponse #匯入http模組
from django.db import connection
from datetime import datetime
from web_tool import models, forms
from web_tool.models import GeneTbl
from django.core.paginator import Paginator, EmptyPage
import pandas as pd
import sys
import time
import json 

sys.path.append("/home/tewer/Web_Project/data")
from data import WebCrawler
def index(request):
    transcript = request.GET.get("transcriptid",False)
    # print(transcript)
    try:
        tr = models.GeneTbl.objects.get(transcriptid__contains=transcript)
        WebCrawler.scrap(transcript)
        df = pd.read_csv("data/turn.csv")
        df1 = pd.read_csv("data/turn1.csv")
        df2 = pd.read_csv("data/turn2.csv")
        with open("data/hw4.txt") as f:
            tempdf2 = f.read()
        f.close()
        df.rename(columns={
            "Name: ": "name",
            "Start: ": "st",
            "End: ": "ed",
            "Length: ": "size"})
        df1.rename(columns={
            "Name: ": "name",
            "Start: ": "st",
            "End: ": "ed",
            "Length: ": "size"
        })
        df2.rename(columns={
            "cds1":"cds1",
            "cds2":"cds2",
            "cds3":"cds3",
            "cds4":"cds4",
            "cds5":"cds5"
        })
        df3 = df2[df2.notnull().all(1)]
        json_string = df.to_json(orient="records")
        json_string1 = df1.to_json(orient="records")
        json_string2 = df3.to_json(orient="records")
        h1 = json.loads(json_string)
        h2 = json.loads(json_string1)
        h3 = json.loads(json_string2)
    except:
        return render(request,"error.html",locals())
    return render(request, "form.html",locals())

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def pag(request):
    genes = models.GeneTbl.objects.all()
    paginator = Paginator(genes,100)
    pageNum = request.GET.get("page")
    try:
        genes = paginator.get_page(pageNum)
    except:
        return render(request,"error.html",locals())
    context = {"genes" : genes}
    return render(request, "WebDev.html",context) 
    
def ajax_data(request):
    char_to_replace = {"'":"",
                   '[': '',
                   ']': ''}
    gene_id = request.POST.get('gene_id',False)
    try:
        gene = models.GeneTbl.objects.get(geneid=gene_id)
        temp = gene.transcriptid
        temp1 = temp.translate(str.maketrans(char_to_replace)) 
        transcript = temp1.split(",")
        numbers = gene.numbers
        dd = {"geneid":gene_id,
                "transcript":transcript,
                "numbers":numbers}
        df = pd.DataFrame(dd)
        message = df.to_json(orient="records")
    except:
        try:
            gene = GeneTbl.objects.get(transcriptid__contains=gene_id)
            temp = gene.transcriptid
            temp1 = temp.translate(str.maketrans(char_to_replace)) 
            transcript = temp1.split(",")
            # print(transcript)
            numbers = gene.numbers
            dd = {"geneid":gene.geneid,
                    "transcript":transcript,
                    "numbers":numbers}
            df = pd.DataFrame(dd)
            # print(df)
            message = df.to_json(orient="records")
        except:
            temp = '{"failed":"Failed..."}'
            message = "Failed..."
        
    response = {
        "message" : message
    }
    return JsonResponse(response)
    