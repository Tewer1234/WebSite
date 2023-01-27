from hmac import trans_5C
# from types import 
import types
from matplotlib.font_manager import json_load
import urllib.request as request
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import sys
# sys.path.append("/home/tewer/Web_Project/data")
# import pythonHw2 as p2
# import pythonHw3 as p3
# import pythonHw4 as p4
# import Scraper as sc

def scrap(transcript):
    URL = "https://wormbase.org/rest/widget/transcript/" + transcript + "/sequences"
    req = request.Request(URL,headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})


    with request.urlopen(req) as response:
            data = response.read().decode("utf-8")
    data = json.loads(data)
    
    # print(data)
    ssequence = ""
    opp = ""
    ustart = []
    uend = []
    utype = []
    usize = []
    sstart = []
    send = []
    stype = []
    ssize = []
    protein = data["fields"]["protein_sequence"]["data"]
    if (data["fields"]["unspliced_sequence_context"]["data"]["strand"]=="-"):
        unspliced = data["fields"]["unspliced_sequence_context"]["data"]["negative_strand"]["features"]
        usequence = data["fields"]["unspliced_sequence_context"]["data"]["negative_strand"]["sequence"]
    else:
        unspliced = data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["features"]
        usequence = data["fields"]["unspliced_sequence_context"]["data"]["positive_strand"]["sequence"]
        
    if (data["fields"]["spliced_sequence_context"]["data"]["strand"]=="+"):
        spliced = data["fields"]["spliced_sequence_context"]["data"]["positive_strand"]["features"]
        ssequence = data["fields"]["spliced_sequence_context"]["data"]["positive_strand"]["sequence"]
        opp = data["fields"]["spliced_sequence_context"]["data"]["negative_strand"]["sequence"]
    else:
        spliced = data["fields"]["spliced_sequence_context"]["data"]["negative_strand"]["features"]
        ssequence = data["fields"]["spliced_sequence_context"]["data"]["negative_strand"]["sequence"]
        opp = data["fields"]["spliced_sequence_context"]["data"]["positive_strand"]["sequence"]
    
    for i in range(len(unspliced)):
        ustart.append(unspliced[i]["start"])
        uend.append(unspliced[i]["stop"])
        utype.append(unspliced[i]["type"])
        usize.append(uend[i]-ustart[i]+1)
    
    for i in range(len(spliced)):
        sstart.append(spliced[i]["start"])
        send.append(spliced[i]["stop"])
        stype.append(spliced[i]["type"])
        ssize.append(send[i]-sstart[i]+1)
    
    # if ("five_prime_UTR" in stype):
    #     for i in range(len(unspliced)):
    #         if (utype[i] == "exon"):
    #             ustart[i]+=1
        
        # for i in range(len(spliced)):
        #     if (stype[i] == "exon"):
        #         sstart[i]+=1
    
    if (("three_prime_UTR" in stype) and ("five_prime_UTR" in stype)):
        # print(stype.index("five_prime_UTR"))
        sstart.append(send[stype.index("five_prime_UTR")]+1)
        send.append(sstart[stype.index("three_prime_UTR")]-1)
        stype.append("CDS")
        ssize.append(sstart[stype.index("three_prime_UTR")]-(send[stype.index("five_prime_UTR")]+1))
    
    
    udd = {
        "Type": utype,
        "Start":ustart,
        "End": uend,
        "Length": usize,
        "Sequence": usequence
    }
    
    sdd = {
        "Type":stype,
        "Start":sstart,
        "End":send,
        "Length":ssize,
        "Sequence": ssequence
    }
    
    temp = ""
    ary = list()
    cnt = 0
    # print(str(protein))
    if (str(protein)!="None"):
        protein = data["fields"]["protein_sequence"]["data"]["sequence"]
        for i in range(len(protein)):
            temp+=protein[i]
            cnt+=1
            if (i%10 == 9):
                if (cnt==50):
                    ary.append(temp)
                    cnt=0
                    temp=""
                else:
                    temp+=" "
        protein=ary
        df3 = pd.DataFrame(protein)
    else:
        ary.append("None")
        df3 = pd.DataFrame(ary)
    df1 = pd.DataFrame(udd)
    df2 = pd.DataFrame(sdd)
    df1.to_csv("/home/tewer/Web_Project/data/turn.csv")
    df2.to_csv("/home/tewer/Web_Project/data/turn1.csv")
    df3.to_csv("/home/tewer/Web_Project/data/turn2.csv")
    return (ssequence,opp,df2)
# scrap("F56A12.3a")




