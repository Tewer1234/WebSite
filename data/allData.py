import pandas as pd
import numpy

ary=list()
with open("/home/tewer/下載/c_elegans.PRJNA13758.WS285.geneOtherIDs.txt") as f:
    flag=1
    geneid={}
    status={}
    sequence={}
    geneName={}
    otherName={}
    while (flag):
        s=f.readline()
        if (len(s)==0):
            flag=0
            break
        else:
            data = s.split("\t")
            for i in range(0,5):
                if (data[i]==""):
                    data[i]="Nan"
            
            ary.append(data[0])
            geneid[data[0]]=data[0]
            status[data[0]]=data[1]
            sequence[data[0]]=data[2]
            geneName[data[0]]=data[3]
            otherName[data[0]]=data[4][:len(data[4])-1]

dd = {
    "Gene ID":geneid,
    "Status":status,
    "Sequence":sequence,
    "Gene Name":geneName,
    "Other Name":otherName
}

df = pd.DataFrame(dd)
df.rename_axis("Index").reset_index()
# print(df)
df.to_csv("/home/tewer/Web_Project/data/dataTable.csv")
f.close()


char_to_replace = {"'":"",
                   '[': '',
                   ']': '',
                   ' ':'',
                   '"':""}
def translation(s):
    temp = s.find("]")
    t = s[:temp]
    t = t.translate(str.maketrans(char_to_replace)) 
    t = t.split(",")
    return (temp,t)

with open("/home/tewer/Web_Project/data/wormbase_genetranscript W285.csv") as f:
    flag=1
    name = []
    geneid={}
    status={}
    sequence={}
    geneName={}
    otherName={}
    transcriptid = {}
    types = {}
    count = {}
    while (flag):
        s = f.readline()
        if (len(s) == 0):
            flag = 0
            break
        else:
            ary = list()
            for i in range(5):
                temp = s.find(",")
                substr = s[:temp]
                s = s[temp+1:]
                ary.append(substr)
            
            temp = s.find("[")
            s = s[temp:]
            temp = translation(s)
            temptr = temp[1]
            s = s[temp[0]:]
            temp = s.find("[")
            s = s[temp:]
            temp = translation(s)
            temptype = temp[1]
            s = s[temp[0]:]
            rest = s.split(",")
            if (len(rest) == 1):
                ary.append(rest[0])
            else:
                ary.append(rest[1])
            
            for i in range(len(temptr)):
                temp = temptr[i]
                if (temp not in name):
                    name.append(temptr[i])
                    geneid[temp]=list()
                    status[temp]=list()
                    sequence[temp]=list()
                    geneName[temp]=list()
                    otherName[temp]=list()
                    transcriptid[temp] = list()
                    types[temp] = list()
                    count[temp]=list()
                
                
                geneid[temp].append(ary[0])
                status[temp].append(ary[1])
                sequence[temp].append(ary[2])
                geneName[temp].append(ary[3])
                otherName[temp].append(ary[4])
                transcriptid[temp].append(temptr[i])
                types[temp].append(temptype[i])
                # count[temp].append(ary[5])
    
    dd = {
        "Transcript ID": transcriptid,
        "Gene ID":geneid,
        "Status": status,
        "Sequence": sequence,
        "Gene Name": geneName,
        "Other Name": otherName,
        "Types": types
    }
    
    df = pd.DataFrame(dd)
    df.to_csv("/home/tewer/Web_Project/data/dataTable.csv")
    f.close()