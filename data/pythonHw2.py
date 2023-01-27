from operator import index
import numpy as np
import pandas as pd

def displayAll(data):
    with open("/home/tewer/Web_Project/unspliced+UTRTranscriptSequence_{}.fasta".format(data),"r") as f:
        s=f.readline()
        s=f.readline()
        #Initialization
        seqst={}
        seqed={}
        size={}
        last=len(s)-1
        first=1
        head=tail=0
        incnt=excnt=pos=0
        seqst["5'UTR"]=seqed["5'UTR"]=size["5'UTR"]="-"
        seqst["CDS"]=seqed["CDS"]=size["CDS"]="-"
        seqst["3'UTR"]=seqed["3'UTR"]=size["3'UTR"]="-"
        #Traversing through the file
        def traverse (t,p, l, r):
            while (p<len(t) and s[p]>=l and s[p]<=r):
                p+=1
            return p
        #Check if there is a head
        if (s[0]>="a" and s[0]<="z"): head=1
        #Cut the sequences into different introns and exons
        while pos<len(s):
            if (s[pos]>="a" and s[pos]<="z"):
                if head and first:
                    temp="5'UTR"
                    seqst[temp]=pos+1
                    first=0
                else:
                    incnt+=1
                    temp="Intron "+str(incnt)
                    seqst[temp]=pos
                pos=traverse(s,pos,"a","z")
                seqed[temp]=pos
                size[temp]=seqed[temp]-seqst[temp]+1
            else:
                excnt+=1
                temp="Exon "+str(excnt) 
                if excnt==1: seqst[temp]=1
                else: seqst[temp]=pos
                pos=traverse(s,pos,"A","Z",)
                seqed[temp]=pos
                size[temp]=seqed[temp]-seqst[temp]+1
            #Check if there is a tail
            # print(pos," ",len(s),"\n")
            if pos==len(s):
                if s[pos-1]>="a" and s[pos-1]<="z":
                    tail=1
            pos+=1
    f.close()
    if tail:
        tempx="Exon "+str(excnt)
        tempi="Intron "+str(incnt)
        seqst["3'UTR"]=seqed[tempx]+1
        seqed["3'UTR"]=len(s)
        size["3'UTR"]=seqed["3'UTR"]-seqst["3'UTR"]+1
        seqed.update({tempx:len(s)})
        size.update({tempx:seqed[tempx]-seqst[tempx]+1})
        del seqst[tempi]
        del seqed[tempi]
        del size[tempi]
    dd={
        "Start":seqst,
        "End":seqed,
        "Length":size}
    df=pd.DataFrame(dd)
    df2 = df.rename_axis("Name").reset_index()
    fr = open("/home/tewer/Web_Project/data/hw2.txt","w")
    dfString = df2.to_string(header=False)
    fr.write(dfString)
    fr.close()
    df2.to_csv("/home/tewer/Web_Project/data/turn.csv")
    # print(df2)
    f.close()

# displayAll("H03G16.7.1")
                    
                
                
                
                    
                