import numpy as np
import pandas as pd
def ExonOnly(data):
    with open("/home/tewer/Web_Project/unspliced+UTRTranscriptSequence_{}.fasta".format(data),"r") as f:
        s=f.readline()
        s=f.readline()
        seqst={}
        seqed={}
        size={}
        last=len(s)-1
        first=1
        head=tail=0
        incnt=excnt=pos=0
        seqst["5'UTR"]=seqed["5'UTR"]=size["5'UTR"]=0
        seqst["CDS"]=seqed["CDS"]=size["CDS"]=0
        seqst["3'UTR"]=seqed["3'UTR"]=size["3'UTR"]=0
        def traverse (t,p, l, r):
            while (p<len(t) and s[p]>=l and s[p]<=r):
                p+=1
            return p
        if (s[0]>="a" and s[0]<="z"): head=1
        while pos<len(s):
            if (s[pos]>="a" and s[pos]<="z"):
                if head and first:
                    temp="5'UTR"
                    seqst[temp]=pos+1
                    first=0
                    pos=traverse(s,pos,"a","z")
                    seqed[temp]=pos
                    size[temp]=seqed[temp]-seqst[temp]+1
            elif (s[pos]>="A" and s[pos]<="Z"):
                excnt+=1
                temp="Exon "+str(excnt) 
                seqst[temp]=pos
                pos=traverse(s,pos,"A","Z")
                seqed[temp]=pos
                size[temp]=seqed[temp]-seqst[temp]
                if (excnt==1 and head): size[temp]+=size["5'UTR"]+1
            if pos==len(s)-1:
                if s[pos]>="a" and s[pos]<="z": tail=1
            pos+=1
    if tail:
        tempx="Exon "+str(excnt)
        seqst["3'UTR"]=seqed[tempx]+1
        seqed["3'UTR"]=len(s)
        size["3'UTR"]=seqed["3'UTR"]-seqst["3'UTR"]+1
        seqed.update({tempx:len(s)})
        size.update({tempx:seqed[tempx]-seqst[tempx]})

    seqst["CDS"]=seqst["Exon 1"]
    if (seqst["CDS"]==0): seqst["CDS"]+=1
    prev=1
    for keys in seqst:
        if keys[:4]=="Exon":
            seqst[keys]=prev
            seqed[keys]=prev+size[keys]-1
            prev=seqed[keys]+1
        if (keys=="Exon "+str(excnt) and tail):
            seqed["3'UTR"]=seqed[keys]
            seqst["3'UTR"]=seqed[keys]-size["3'UTR"]+1
    seqed["CDS"]=seqed["Exon "+str(excnt)]-size["3'UTR"]
    size["CDS"]=seqed["CDS"]-seqst["CDS"]+1
    if (seqst["5'UTR"]==0): 
        seqst["5'UTR"]='-'
        seqed["5'UTR"]='-'
        size["5'UTR"]='-'
    if (seqst["3'UTR"]==0): 
        seqst["3'UTR"]='-'
        seqed["3'UTR"]='-'
        size["3'UTR"]='-'
    if (seqst["CDS"]==0): 
        seqst["CDS"]='-'
        seqed["CDS"]='-'
        size["CDS"]='-'
    dd={
        "Start":seqst,
        "End":seqed,
        "Length":size}
    df=pd.DataFrame(dd)
    df2 = df.rename_axis("Name").reset_index()
    fr = open("/home/tewer/Web_Project/data/hw3.txt","w")
    dfString = df2.to_string(header=False)
    fr.write(dfString)
    fr.close()
    df2.to_csv("/home/tewer/Web_Project/data/turn1.csv")
    # print("Name",df)
    f.close()