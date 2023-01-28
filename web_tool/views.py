from operator import contains
from os import rename
from unittest.util import _Mismatch
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse #匯入http模組
from django.db import connection
from datetime import datetime
from web_tool import models, forms
from web_tool.models import MrnaTbl,Datatable, W285Table,Browsetable
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
import pandas as pd
import numpy as np
import os
import sys
import time
import json 

sys.path.append("/home/tewer/Web_Project/data")
sys.path.append("/home/tewer/Web_Project/pirScan")
from data import WebCrawler,Scraper
char_to_replace = {"'":"",
                   '[': '',
                   ']': '',
                   ' ':''}

def getPiRNA():
    f = open("/home/tewer/Web_Project/pirScan/output/piRNA_targeting_sites.json")
    df3 = json.load(f)
    name = []
    pos = []
    mismatch = []
    misPos = []
    nonGUseedRegionnum = []
    GUseedRegionnum = []
    nonSeednonGUnum = []
    nonSeedGUnum = []
    site = []
    piRNAdetail = []
    abundance = {}
    rpiRNAseq = []
    
    data = df3["newout"]
    
    for i in range(len(data)):
        sub = data[i]
        name.append(sub[0])
        pos.append(sub[1])
        mismatch.append(sub[2])
        misPos.append(sub[3])
        nonGUseedRegionnum.append(sub[5])
        GUseedRegionnum.append(sub[6])
        nonSeednonGUnum.append(sub[7])
        nonSeedGUnum.append(sub[8])
        site.append(sub[9])
        piRNAdetail.append(sub[10])
        if (sub[0] not in abundance):
            abundance[sub[0]] = list()
            abundance[sub[0]].append(sub[0])
        
        for each in sub[11]:
            abundance[sub[0]].append(each)
        rpiRNAseq.append(sub[12])
    dd = {
        "name": name,
        "pos": pos,
        "mismatch": mismatch,
        "misPos": misPos,
        "nonGUseedRegionnum": nonGUseedRegionnum,
        "GUseedRegionnum": GUseedRegionnum,
        "nonSeednonGUnum": nonSeednonGUnum,
        "nonSeedGUnum": nonSeedGUnum,
        "site": site,
        "piRNAdetail": piRNAdetail,
        "rpiRNAseq": rpiRNAseq
    }

    ab = {
        "name":list(),
        "Tang_smallRNA1":list(),
        "Tang_PRG_1IP1":list(),
        "Gu_PRG_IP2":list(),
        "Lee_small_RNA3":list(),
        "Lee_small_RNAs_prg_1_mutant3":list()
    }
    
    # print(abundance)
    for each in abundance:
        ab["name"].append(each)
        ab["Tang_smallRNA1"].append(abundance[each][1])
        ab["Tang_PRG_1IP1"].append(abundance[each][2])
        ab["Gu_PRG_IP2"].append(abundance[each][3])
        ab["Lee_small_RNA3"].append(abundance[each][4])
        ab["Lee_small_RNAs_prg_1_mutant3"].append(abundance[each][5])
    
    return (dd,ab)

def index(request):
    transcript = request.GET.get("transcriptid2",False)
    # print(transcript)
    
    try:
        seq = WebCrawler.scrap(transcript)
        cds="none"
        if (len(seq[0])>0):
            temp = pd.read_csv("data/turn1.csv")
            temp = temp.to_json(orient="records")
            temp = json.loads(temp)
        
        for each in temp:
            if (each["Type"]=="CDS"):
                cds = str(each["Start"])+"-"+str(each["End"])
                break
            else:
                cds="none"
                
        f = open("/home/tewer/Web_Project/pirScan/inputSeq.txt","w")
        f.write("{}_spliced+UTR\n".format(transcript))
        f.write(seq[0])
        f.close()
        os.chdir("/home/tewer/Web_Project/pirScan")
        os.system("python3 piTarPrediction.py inputSeq.txt ce {} [0,2,2,3,6]".format(cds))
        os.chdir("/home/tewer/Web_Project")
        try:
            arg = getPiRNA()
            df3 = pd.DataFrame(arg[0])
            abundanceTbl = pd.DataFrame(arg[1])
            # print(ab)
            json_string3 = df3.to_json(orient="records")
            json_string4 = abundanceTbl.to_json(orient="records")
            piRNA = json.loads(json_string3)
            piAbundance = json.loads(json_string4)
        except:
            pass
        df = pd.read_csv("data/turn.csv")
        df.loc[len(df.index)] = [0,transcript,0,0,0,"temporary"]
        df1 = pd.read_csv("data/turn1.csv")
        df2 = pd.read_csv("data/turn2.csv")
        
        json_string = df.to_json(orient="records")
        json_string1 = df1.to_json(orient="records")
        json_string2 = df2.to_json(orient="records")
        
        h1 = json.loads(json_string)
        h2 = json.loads(json_string1)
        h3 = json.loads(json_string2)
        
    except:
        return render(request,"error.html",locals())
    return render(request, "form.html",locals())

def index2(request):
    transcript = request.GET.get("transcriptid3",False)
    
    try:
        df = pd.read_csv("data/turn.csv")
        df1 = pd.read_csv("data/turn1.csv")
        df2 = pd.read_csv("data/turn2.csv")
        df.loc[len(df.index)] = [0,transcript,0,0,0,"temporary"]
        
        json_string = df.to_json(orient="records")
        json_string1 = df1.to_json(orient="records")
        json_string2 = df2.to_json(orient="records")
        h1 = json.loads(json_string)
        h2 = json.loads(json_string1)
        h3 = json.loads(json_string2)
        
        seq = WebCrawler.scrap(transcript)
        cds="none"
        if (len(seq[0])>0):
            temp = pd.read_csv("data/turn1.csv")
            temp = temp.to_json(orient="records")
            temp = json.loads(temp)
        
        for each in temp:
            if (each["Type"]=="CDS"):
                cds = str(each["Start"])+"-"+str(each["End"])
                break
            else:
                cds="none"
                
        f = open("/home/tewer/Web_Project/pirScan/inputSeq.txt","w")
        f.write("{}_spliced+UTR\n".format(transcript))
        f.write(seq[0])
        f.close()
        os.chdir("/home/tewer/Web_Project/pirScan")
        os.system("python3 piTarPrediction.py inputSeq.txt ce {} [0,2,2,3,6]".format(cds))
        os.chdir("/home/tewer/Web_Project")
        try:
            arg = getPiRNA()
            df3 = pd.DataFrame(arg[0])
            abundanceTbl = pd.DataFrame(arg[1])
            # print(ab)
            json_string3 = df3.to_json(orient="records")
            json_string4 = abundanceTbl.to_json(orient="records")
            piRNA = json.loads(json_string3)
            piAbundance = json.loads(json_string4)
        except:
            pass
        
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
    # noncoding = NcrnaTbl.objects.all()
    # p = Paginator(noncoding,20)
    # pageNum = request.GET.get('page')
    # noncoding = p.get_page(pageNum)
    genes = models.MrnaTbl.objects.all()
    context = {"genes" : genes}
    return render(request, "WebDev.html",context) 
    
def ajax_data(request):
    
    gene_id = request.POST.get('gene_id',False)
    try:
        gene = models.MrnaTbl.objects.get(geneid=gene_id)
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
            gene = MrnaTbl.objects.get(transcriptid__contains=gene_id)
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

def ajax_data2(request):
    ncode = request.POST.get("gene_id2",False)
    data = Scraper.nCoding(ncode,1)
    # print(gene," \n",type(gene))
    # print(data)
    if (type(data)!=str):  
        ngene = models.W285Table.objects.get(geneid=data[0])
        
        df = pd.read_csv("/home/tewer/Web_Project/data/turn3.csv")
        temp = ngene.transcript.translate(str.maketrans(char_to_replace)) 
        temp1 = temp.split(",")
        temp = ngene.type.translate(str.maketrans(char_to_replace)) 
        temp2 = temp.split(",")
        # print(df["Type"])
        while (len(temp2)<len(df["Transcript"])):
            temp1.append("")
            temp2.append("")
        # print(temp2)
        dd = {
            "input":ncode,
            "Gene ID":df["Gene_ID"],
            "Transcript" : df["Transcript"],
            "Transcript Length (nt)" : df["Transcript_Length_(nt)"],
            "Type" : df["Type"],
            "Coding Sequence (CDS)" : df["Coding_Sequence_(CDS)"],
            "Coding Sequence Length (nt)" : df["Coding_Sequence_Length_(nt)"],
            "Protein" : df["Protein"],
            "Protein Length (aa)" : df["Protein_Length_(aa)"],
            "Status":ngene.status,
            "Sequence":ngene.sequence,
            "Gene Name":ngene.genename,
            "Other Name":ngene.othername,
            "transcript":temp1,
            "type":temp2,
            "Transcript Count":ngene.transcript_count
        }
        df2 = pd.DataFrame(dd)
        message2 = df2.to_json(orient="records")
    else:
        if (data=="A lot"):
            message2 = "Multiple results found, please be more specific"
        else:
            message2 = "Failed..."
    response = {
        "message2": message2
    }
    return JsonResponse(response)
    
def ajax_data3(request):
    method = request.POST.get("method",False)
    message3=method
    # print(message3)
    response = {
        "message3":message3
    }
    return JsonResponse(response)

def change(s):
    t = s
    t = t.translate(str.maketrans(char_to_replace))
    return t


def browse_data(request):
    ncode = request.POST.get("transcriptType",False)
    # data = Scraper.nCoding(ncode,2)
    cnt = 0
    name1 = []
    geneid1 = {}
    status1 = {}
    transcriptid1 = {}
    sname1 = {}
    genename1 = {}
    other1 = {}
    types1 = {}
    pnum = {}
    pstart = {}
    plimit = {}
    total = {}
    # print(data)
    # for each in data[1]:
    # print(ncode)
    gene = models.Browsetable.objects.filter(types__contains=ncode)
    length = len(gene)
    # print(legn)
    # paginator = Paginator(gene,20)
    # pageNum = request.GET.get('page')
    # maxNum = paginator.num_pages
    # gene = paginator.get_page(pageNum)
    for each in gene:
        temp = each.types
        temp = temp.translate(str.maketrans(char_to_replace)) 
        # print(temp)
        if (temp == ncode):
            temp = each.transcriptid
            temp = temp.translate(str.maketrans(char_to_replace)) 
            # print(temp)
            if (temp not in name1):
                name1.append(temp)
            
            cnt+=1
            pstart[temp] = 1
            # plimit[temp] = maxNum
            pnum[temp] = cnt//20
            total[temp] = length
            geneid1[temp]=(change(each.geneid))
            status1[temp]=(change(each.status) )
            transcriptid1[temp]=(change(each.transcriptid)  )
            sname1[temp]=(change(each.sequence)  )
            genename1[temp]=(change(each.genename)  )
            other1[temp]=(change(each.othername) )
            types1 [temp]=(change(each.types)  )
    # print(geneid1)
    dd = {
        "Gene ID" : geneid1,
        "Status" : status1,
        "Sequence" : sname1,
        "Gene Name" : genename1,
        "Other Name" : other1,
        "Transcript" : transcriptid1,
        "Type" : types1,
        "Page Num": pnum,
        "Page Start": pstart,
        "Page End": plimit,
        "Total": total
    }
    
    df = pd.DataFrame(dd)
    # print(df)
    message = df.to_json(orient="records")
    
    response = {
        "message4":message,
    }
    # print(gene)
    return JsonResponse(response)

def readCSV(request):
    df1 = pd.read_csv("data/turn.csv")
    message = df1.to_json(orient="records")
    response = {
        "message":message
    }
    # print(df1)
    return JsonResponse(response)