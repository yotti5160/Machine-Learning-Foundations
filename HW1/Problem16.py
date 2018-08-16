#read file 
import random
f = open("C:/Users/Yotti/Desktop/機器學習基石/HW1data/PLAdata.txt","r")
data = []
for line in f:
    tmp=line.split()
    tmpNum=[1] #x0=1 for all data
    for t in tmp:
        tmpNum.append(float(t))
    data.append(tmpNum)  

#generating random ordered data
def changeDataOrder(data):
    tmpdata=list.copy(data)
    random.shuffle(tmpdata)
    return tmpdata
    
#PLA 
def sign(x): return 1 if x>0 else -1

def PLA(data):
    w=[0,0,0,0,0]
    allcorrect=False
    count=0
    while not allcorrect:
        allcorrect=True
        for d in data:
            tmp=sign(w[0]*d[0]+w[1]*d[1]+w[2]*d[2]+w[3]*d[3]+w[4]*d[4])
            if tmp!=d[5]:
                count+=1
                allcorrect=False
                for i in range(5):
                    w[i]+=0.5*d[5]*d[i]
    return count

#random ordered PLA 2000 times
totalTimes=0
for i in range(2000):    
    totalTimes+=PLA(changeDataOrder(data))
print(totalTimes/2000)
