def sign(x): return 1 if x>0 else -1

#read file 
def readFile(location):
    f = open(location,"r")
    dx, dy = [], []
    for line in f:
        tmp=line.split()
        tmpx, tmpy=tmp[0:9], float(tmp[9])
        for i in range(len(tmpx)):
            tmpx[i]=float(tmpx[i])
        dx.append(tmpx)
        dy.append(tmpy)
    f.close()
    return [dx, dy]

def runDSA(rx,ry):
    bestS, bestTheta, ER=0,0,2
    tmp=ry.count(1)/len(rx)
    if tmp<ER:
        bestS=-1
        bestTheta=min(rx)
        ER=tmp
    tmp=ry.count(-1)/len(rx)
    if tmp<ER:
        bestS=1
        bestTheta=min(rx)
        ER=tmp
    
    for i in range(len(rx)-1):
        threshold=(rx[i]+rx[i+1])/2
        for s in [-1,1]:
            tmpER=0
            for index in range(len(rx)):
                if ry[index]!=s*sign(rx[index]-threshold):
                    tmpER+=1
            tmpER/=len(rx)
            if tmpER<ER:
                ER=tmpER
                bestS=s
                bestTheta=threshold
    return [bestS, bestTheta, ER]


loc='C:/Users/Yotti/Desktop/機器學習基石/HW2data/training.txt'
TMP=readFile(loc)
dx, dy=TMP[0], TMP[1]

besti, bestS, bestTheta, ER=0,0,0,2

for i in range(9):
    tmpdata=[]
    for j in range(len(dx)):
        tmpdata.append([dx[j][i], dy[j]])
    tmpdata=sorted(tmpdata, key=lambda d: d[0])
    tmpx, tmpy=[], []
    for t in tmpdata:
        tmpx.append(t[0])
        tmpy.append(t[1])
    TMP=runDSA(tmpx,tmpy)
    if TMP[2]<ER:
        ER=TMP[2]
        besti=i
        bestS=TMP[0]
        bestTheta=TMP[1]

loc2='C:/Users/Yotti/Desktop/機器學習基石/HW2data/test.txt'
TMP2=readFile(loc2)
testX, testY=TMP2[0], TMP2[1]
Eout=0
for i in range(len(testX)):
    if testY[i]!=bestS*sign(testX[i][besti]-bestTheta):
        Eout+=1
print(Eout/len(testY))






