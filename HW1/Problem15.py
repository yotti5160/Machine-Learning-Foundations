#read file 
f = open("C:/Users/Yotti/Desktop/機器學習基石/HW1data/PLAdata.txt","r")
data = []
for line in f:
    tmp=line.split()
    tmpNum=[1] #x0=1 for all data
    for t in tmp:
        tmpNum.append(float(t))
    data.append(tmpNum)  

#PLA 
def sign(x): return 1 if x>0 else -1
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
                w[i]+=d[5]*d[i]

print(count)
print(w)
