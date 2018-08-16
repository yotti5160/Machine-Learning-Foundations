import random
import time

#read file 
def readFile(location):
    f = open(location,"r")
    data = []
    for line in f:
        tmp=line.split()
        tmpNum=[1] #x0=1 for all data
        for t in tmp:
            tmpNum.append(float(t))
        data.append(tmpNum) 
    f.close()
    return data

#generating random ordered data
def changeDataOrder(data):
    tmpdata=list.copy(data)
    random.shuffle(tmpdata)
    return tmpdata
    
#sign
def sign(x): return 1 if x>0 else -1

#pocket PLA return pocketW
def PocketPLA(TrainingData, standard):
    updateCount=0
    w=[0,0,0,0,0]
    pocketW=[0,0,0,0,0]
    pocketER=checkER(TrainingData, pocketW)
    allcorrect=False
    
    while updateCount<standard and not allcorrect:
        allcorrect=True
        for d in TrainingData:
            if d[5]!=sign(w[0]*d[0]+w[1]*d[1]+w[2]*d[2]+w[3]*d[3]+w[4]*d[4]):
                for i in range(5):
                    w[i]+=d[5]*d[i]
                tmpER=checkER(TrainingData, w)
                if tmpER<pocketER:
                    pocketW=list.copy(w)
                    pocketER=tmpER
                allcorrect=False
                updateCount+=1
                if updateCount>=standard:
                    return pocketW
    return pocketW

#check error rate
def checkER(data, w):
    errorNum=0
    for d in data:
        if d[5]!=sign(w[0]*d[0]+w[1]*d[1]+w[2]*d[2]+w[3]*d[3]+w[4]*d[4]):
            errorNum+=1
    return errorNum/len(data)

def main(NumOfRun):
    #read training data and test data
    trainingData=readFile("C:/Users/Yotti/Desktop/機器學習基石/HW1data/trainingData.txt")
    testData=readFile("C:/Users/Yotti/Desktop/機器學習基石/HW1data/testData.txt")

    avgER=0
    for i in range(NumOfRun):
        tmpTrainingData=changeDataOrder(trainingData)
        tmpw=PocketPLA(tmpTrainingData, 50) #  PocketPLA with 50 updates 
        avgER+=checkER(testData, tmpw)
    return avgER/NumOfRun

#starts here
start_time = time.time()
print(main(200))
print("--- %s seconds ---" % (time.time() - start_time))
