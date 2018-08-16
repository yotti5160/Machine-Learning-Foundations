import random as r

def sign(x): return 1 if x>0 else -1

def genData(DataSize):
    rx, ry = [], []
    for i in range(DataSize):
        rx.append(r.uniform(-1,1))
    rx.sort()
    for d in rx:
        tmp=r.random()
        if d>0:
            if tmp<0.2:
                ry.append(-1)
            else:
                ry.append(1)
        else:
            if tmp<0.2:
                ry.append(1)
            else:
                ry.append(-1)
    return [rx,ry]

def runDSA(rx,ry):
    bestS, bestTheta, ER=0,0,2
    tmp=ry.count(1)/len(rx)
    if tmp<ER:
        bestS=-1
        bestTheta=-1.1
        ER=tmp
    tmp=ry.count(-1)/len(rx)
    if tmp<ER:
        bestS=1
        bestTheta=-1.1
        ER=tmp
    
    for i in range(len(rx)-1):
        threshold=(rx[i]+rx[i+1])/2
        for s in [-1,1]:
            tmpER=0
            for index in range(len(rx)):
                if ry[index]!=s*sign(rx[index]-threshold):
                    tmpER+=1
            tmpER/=20
            if tmpER<ER:
                ER=tmpER
                bestS=s
                bestTheta=threshold
    return [bestS, bestTheta]

def main(times):
    Eout=0
    for i in range(times):
        TMP=genData(20)
        rx, ry=TMP[0], TMP[1]
        Ret=runDSA(rx,ry)
        Eout+=(0.5+0.3*Ret[0]*(abs(Ret[1])-1))
    return Eout/times

print(main(5000))
            
