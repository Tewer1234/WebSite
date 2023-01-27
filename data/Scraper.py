from hmac import trans_5C
# from types import 
import types
from matplotlib.font_manager import json_load
import urllib.request as request
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from web_tool.models import W285Table
from django.db.models import Q


def ExtractData(series):
    ary = list()
    size = len(series[0])
    if (size==0):
        ary.append("None")
    else:
        for i in series[0]:
            ary.append(i)
    return ary


def nCoding(data,method):
    types = dict()
    length_unspliced = dict()
    protein =dict()
    length_protein = dict()
    length_spliced = dict()
    geneid = dict()
    cds = dict()
    transcriptid =dict()
    numbers = {0}
    gene = W285Table.objects.filter(
        Q(geneid__contains=data) |
        Q(sequence__contains=data) |
        Q(genename__contains=data) |
        Q(othername__contains=data) |
        Q(transcript__contains=data) |
        Q(type__contains=data)
    )
    try:
        if (len(gene)==1):
                data = gene[0].geneid
                url = "https://wormbase.org/rest/widget/gene/" + data + '/sequences'
                req = request.Request(url,headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
                with request.urlopen(req) as response:
                    sequence = response.read().decode("utf-8")
                sequence = json.loads(sequence)
                # print(sequence)
                # print(len(sequence["fields"]["gene_models"]["data"]["table"]))
                for i in range(len(sequence["fields"]["gene_models"]["data"]["table"])):
                        # print(sequence["fields"]["gene_models"]["data"]["table"][i])
                        if (data not in types):
                            types[data]=list()
                            length_unspliced[data]=list()
                            protein[data]=list()
                            length_protein[data]=list()
                            length_spliced[data]=list()
                            geneid[data]=list()
                            transcriptid[data]=list()
                            cds[data]=list()
                        if (i != len(sequence["fields"]["gene_models"]["data"]["table"])-1):
                            types[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["type"])
                            length_unspliced[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["length_unspliced"])
                            try:
                                transcriptid[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["model"][0]["id"])
                            except:
                                transcriptid[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["model"]["id"])
                        else:
                            if (len(sequence["fields"]["gene_models"]["data"]["table"][i]["type"])>=1):
                                types[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["type"][0])
                                length_unspliced[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["length_unspliced"][0])
                                try:
                                    transcriptid[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["model"][0]["id"]) 
                                except:
                                    transcriptid[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["model"]["id"])
                        length_spliced[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["length_spliced"])
                        geneid[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["gene"]["id"])
                        temp=str(sequence["fields"]["gene_models"]["data"]["table"][i]["protein"])
                        if (temp!="None"):
                            protein[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["protein"]["label"])
                            length_protein[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["length_protein"])
                        else:
                            protein[data].append("None")
                            length_protein[data].append("None")
                        if (str(sequence["fields"]["gene_models"]["data"]["table"][i]["cds"])=="(no CDS)"):
                            cds[data].append("(no CDS)")
                        else:
                            cds[data].append(sequence["fields"]["gene_models"]["data"]["table"][i]["cds"]["text"]["label"])
                dd = {
                    "Gene_ID" : geneid,
                    "Transcript" : transcriptid,
                    "Transcript_Length_(nt)" : length_unspliced,
                    "Type" : types,
                    "Coding_Sequence_(CDS)" : cds,
                    "Coding_Sequence_Length_(nt)" : length_spliced,
                    "Protein" : protein,
                    "Protein_Length_(aa)" : length_protein,
                }

                df = pd.DataFrame(dd)
                df2 = df.rename_axis("Name").reset_index()
                temp = ExtractData(df2["Transcript"])
                temp1 = ExtractData(df2["Transcript_Length_(nt)"])
                temp2 = ExtractData(df2["Type"])
                temp3 = ExtractData(df2["Coding_Sequence_(CDS)"])
                temp4 = ExtractData(df2["Coding_Sequence_Length_(nt)"])
                temp5 = ExtractData(df2["Protein"])
                temp6 = ExtractData(df2["Protein_Length_(aa)"])
                temp7 = ExtractData(df2["Gene_ID"])
                tempd = {
                    "Gene_ID" : temp7,
                    "Transcript" : temp,
                    "Transcript_Length_(nt)" : temp1,
                    "Type" : temp2,
                    "Coding_Sequence_(CDS)" : temp3,
                    "Coding_Sequence_Length_(nt)" : temp4,
                    "Protein" : temp5,
                    "Protein_Length_(aa)" : temp6,
                }
                res = pd.DataFrame(tempd)
                df2 = res.rename_axis("Name").reset_index()
                df2.to_csv("/home/tewer/Web_Project/data/turn3.csv")
                return (data,df2)
        elif (len(gene)==0):
            return "There is an error to your input, please try again"
        else:
            if (method==2):
                temp = list()
                for each in gene:
                    temp.append(each.geneid)
                return (data,temp)
            else:
                return "A lot"
    except:
        return "There is an error to your input, please try again"

# print(nCoding("WBGene00000001",1))