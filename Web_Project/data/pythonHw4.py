import pandas as pd
def CDS(data):
    acid="FFLLSSSSYY//CC/WLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    base="UCAG"
    codon=""
    finalCDS=spliced=""
    pos=cnt=amount=0
    first=1
    seq={}
    for i in range(len(base)):
        for j in range(len(base)):
            for k in range(len(base)):
                codon=base[i]+base[j]+base[k]
                seq[codon]=acid[pos]
                pos+=1
    with open("/home/tewer/Web_Project/unspliced+UTRTranscriptSequence_{}.fasta".format(data),"r") as f:
        t=f.readline()
        t=f.readline()
        s=t.replace("T","U")
        cur=size=0
        while cur<len(s):
            if (s[cur]>='A' and s[cur]<='Z'): spliced+=s[cur]
            cur+=1
        for i in range(0,len(spliced)-1,3):
            temp=spliced[i:i+3]
            if seq[temp]!="/": finalCDS+=seq[temp]
    size=len(finalCDS)
    fr=open("/home/tewer/Web_Project/data/hw4.txt","w")
    temp = "cds1,cds2,cds3,cds4,cds5\n"
    # temp = "> Conceptual Translation {} aa\n".format(len(finalCDS))
    for i in range(0,len(finalCDS)):
        temp = temp+finalCDS[i]
        amount+=1
        if (first):
            first=0
            continue
        if amount%10==0:
            cnt+=1
            amount=0
            if (cnt==5):
                temp+="\n"
                cnt=0
            else:
                temp+=","
    fr.write(temp)
    fr.close()
    import csv
    with open('/home/tewer/Web_Project/data/hw4.txt') as report:
        reader = csv.reader(report, delimiter=",")
        with open('/home/tewer/Web_Project/data/turn2.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in reader:
                writer.writerow(line)
    csvfile.close()
    report.close()
    # data = pd.read_csv("hw4.txt",delimiter=",")
    # data.columns = ["cds1"]
    # data.to_csv("turn2.csv",index=None)
    # print(data)
    f.close()

# CDS("F41G4.13.1")