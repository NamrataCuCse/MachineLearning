def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step 

pattern = int(input("Enter no of patterns: "))
col = int(input("Enter no of columns: "))
cluster = int(input("Enter no of clusters: "))
dataSet = []
##print (pattern, col, cluster)

for i in range(pattern):
    p = []

    for j in range(col+1):
        if(j < col):
            print("Possible Column Values 0,1 ")
            p.append(int(input("Enter Column value: ")))
        else:
            print ("Possible Cluster Values upto " ,cluster)
            p.append(int(input("Enter Cluster value: ")))

    dataSet.append(p)
print("Dataset")
print(dataSet)

#learningRate = float(input("Enter Learing Rate: "))
#k1 = float(input("Enter K: "))

##weight matrix generation

q = []
for i in range(pattern):
    q.append(dataSet[i][col])
    
uniqueCluster = set(q)
weight = []
actualPattern=[]
for i in uniqueCluster:
    for j in range(len(dataSet)):
        if(dataSet[j][col] == i):
            weight.append(dataSet[j])
            actualPattern.append(j)
            break
print("Weight & Actual Pattern")
print(weight,actualPattern)
actualWeight=[]

for i in range(col):
    tmp=[]
    for j in range(len(weight)):
        tmp.append(weight[j][i])
    print("tmp is: ",tmp)#
    actualWeight.append(tmp)
    print("After appending tmp weight matrix is: ",actualWeight)#
    del(tmp)
print("Weight Matrix")
print(actualWeight)
copyWeight=actualWeight.copy()



##create sum
sum=[]
for i in range(cluster):
    sum.append(0)

def findMin(sum,j):
    min=sum[0]
    index=0
    for i in range(1,j):
        if(min>=sum[i]):
            index=i
    return index

def setValue(sum,j):
    for i in range(j):
        sum[i]=0


for learningRate1 in frange(0.1,0.9,0.1):
    for k1 in frange(0.1,0.9,0.1):
        p=1
        flag=1
        actualWeight=copyWeight.copy()
        learningRate=learningRate1
        print()
        print()
        print()
        while(1):
            print("For learning rate =", learningRate, " & k=",k1)
            if(flag):
                for i in range(pattern):
                    if i not in actualPattern:
                        print("pattern ",i+1)
                        for j in range(cluster):
                            for k in range (col):
                                sum[j]+=(dataSet[i][k]-actualWeight[k][j])*(dataSet[i][k]-actualWeight[k][j])
                        print("D1, D2, ...")
                        print(sum)
                            
                        j=findMin(sum,cluster)
                        print("Index", j+1)
                        
                        if(j+1==dataSet[i][col]):
                            for k in range(col):
                                actualWeight[k][j]+=learningRate*(dataSet[i][k]-actualWeight[k][j])
                        else:
                            for k in range(col):
                                actualWeight[k][j]-=learningRate*(dataSet[i][k]-actualWeight[k][j])
                                p=0
                        print("Updated Weight Matrix")
                        print(actualWeight)
                        setValue(sum,cluster)
                flag=0
            else:
                for i in range(pattern):
                    if i not in actualPattern:
                        print("pattern ",i+1)
                        for j in range(cluster):
                            for k in range (col):
                                sum[j]+=(dataSet[i][k]-actualWeight[k][j])*(dataSet[i][k]-actualWeight[k][j])
                        print("D1, D2, ...")
                        print(sum)
                            
                        j=findMin(sum,cluster)
                        print("Index", j+1)
                        
                        if(j+1==dataSet[i][col]):
                            for k in range(col):
                                actualWeight[k][j]+=learningRate*(dataSet[i][k]-actualWeight[k][j])
                        else:
                            for k in range(col):
                                actualWeight[k][j]-=learningRate*(dataSet[i][k]-actualWeight[k][j])
                                p=0
                        print("Updated Weight Matrix")
                        print(actualWeight)
                        setValue(sum,cluster)
            print("Value of k1 is: ",k1)
            learningRate*=k1

            if(p==1):
                break
            else:
                p=1
            
            

                    
        print("Final Result")
        print(actualWeight)
