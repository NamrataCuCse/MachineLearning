
import numpy as np

with open('inputdata.txt', 'r') as file:
    file.readline() # skip the first line
    rows = [[int(x) for x in line.split(' ')] for line in file] 
    cols = [list(col) for col in zip(*rows)] 
    print("\nInput Dataset ::")
    print(cols)   
    
    
n1 = len(cols[0]) #no. 0f rows
print("\nMean of [Sample-A  Sample-B] ::")
mean=np.mean(cols, axis=1) 
print(mean)
print("\nVariance of [Sample-A  Sample-B] ::")
var_a =np.var(cols, axis=1,ddof=1) 
print(var_a)
sum=0
print("\nStandard Deviation of the difference between the means ::")
stddev = np.sqrt((var_a[0] + var_a[1])/n1) 
print(stddev)

print("\nt-Value ::")
if var_a[0]>var_a[1]:
 t = (mean[0] - mean[1])/stddev
else:
 t = (mean[1] - mean[0])/stddev  
print(t)


b = open("t_test_table", "r").readlines()   
temp = []
arr=[] #sliced list
line = b[0].split()
temp.append(line)
print("\ndegree of freedom ::")
df=2*n1-2 #degree of freedom
if df>120:
    df=120
print(df)
line = b[df].split()
temp.append(line)
arr.append(temp[0][1:])
arr.append(temp[1][1:])

ts=arr[1]

if(t<=ts[0]):
    thing_index=0
elif (t>ts[0] and t<=ts[1]):
    thing_index=1
elif (t>ts[1] and t<=ts[2]):
    thing_index=2
elif (t>ts[2] and t<=ts[3]):
    thing_index=3
elif (t>ts[3] and t<=ts[4]):
   thing_index=4
else:
     thing_index=5

print("\np-Value ::")
kl=arr[0][thing_index]
print(kl)


print("\nOutput ::")


if float(kl) == 0.200:
    print("Less Significant(80%)") 
elif float(kl) == 0.100:
    print("Significant(90%)") 
elif float(kl) == 0.050:
    print("Moderately Significant(95%)")  
elif float(kl) == 0.020:
    print("Highly Significant(98%)")
elif float(kl) == 0.010:
    print("Highly Significant(99%)") 
else:
    print("Very Highly Significant(99.99%)")

