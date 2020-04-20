import math

w=[]
o=[]
error=[]
q=[]
I=[]
sum=0
#l=0.5
e=2.72818285
t=1

def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step 


#input the number of vertices
n_start= int(input("Enter no of outer vertices: "))
n_in= int(input("Enter no of inner vertices: "))
n_end= int(input("Enter no of end vertices: "))
it= int(input("Enter no of iterations: "))

#taking actual input the value of start vertices
for i in range(0, n_start):
    print("Enter Value for I[%d] :"%(i+1))
    o.append(float(input()))
print("\nTRAINING PATTERN : \n",o)
print("\n")

#input the weight from start to inner

for i in range(0, n_start):
    for j in range(n_start,(n_in+n_start)):
        print("Enter Value for w[%d][%d] :"%((i+1),(j+1)))
        w.append(float(input()))
       
        
#input the weight from inner to end
for i in range(0, n_in):
    for j in range(0,n_end):
        print("Enter Value for w[%d][%d] :"%((n_start+i+1),(n_start+n_in+j+1)))
        w.append(float(input()))
print("\nINITIAL WEIGHTS : \n",w)
print("\n")

#input the theta value
for i in range(0, (n_in+n_end)):
    print("Enter Value for q[%d] :"%(i+n_start+1))
    q.append(float(input()))
print("\nINITIAL BIAS : \n",q)


for m in range(0,it):
   # set I and O for inner layer
    for i in range(0,n_in):
        for j in range(0,n_start):
            sum=sum+(w[(j*n_in)+i]*o[j])

        print("\nNET INPUT AND ACTIVATION OF [%d]th NEURON : \n"%(i + n_start+1))  
        I.append(sum+q[i])
        print("input I[%d] = %s"%((i + n_start+1),I[i]))
        pt=1/(1 + math.exp(-I[i]))  
        o.append(pt)
        print("output O[%s] = %s"%((i + n_start+1),o[i + n_start]))
        sum=0

        
#set I and O for end layer
    sum=0
    for i in range(0,n_end):
        for j in range(0,n_in):
            sum = sum + (w[(n_start * n_in) + j] * o[j + n_start])
        print("\n\nNET INPUT AND ACTIVATION OF [%d]th NEURON : \n"%(i + n_start+n_in+1))  
        I.append(sum + q[n_in + i])
        print("input I[%d] = %s \n"%((i + n_start + n_in+1),I[i + n_in]))	
        qt=1 / (1 + math.exp(-I[n_in +i]))
        o.append(qt)
        sum=0
        print("output O[%d] =%s "%((i + n_start+n_in+1), o[n_in + n_start + i]))
			
#error calculation for n_end i.e. last layer
    print("\nERROR : \n") 
    for i in range(0,n_end):
        me=o[n_start+n_in+i]*(1-o[n_start+n_in+i])*(t-o[n_start+n_in+i])
        error.append(me)
        print("error[%d] = %s"%((n_start+n_in+i +1),error[i]))

#error calculation for n_in or hidden layer

    sum=0
    for i in reversed(range(0,n_in)):
        for j in range(0,n_end):
            sum = sum + error[j] * w[(n_start * n_in) + i]				

        pe=o[n_start + i]*(1 - o[n_start + i])*sum
        error.append(pe)
        print("error[%d] = %s "%( (n_start+i+1), error[n_in-i]))
        sum=0
			
#new path weight
    
    k=0
    print("\nNEW WEIGHT : \n") 
    for i in range(0,n_start):
        for j in range(0,n_in):
            w[k]=w[k]+(l*error[n_in-j]*o[i])
            if m<it:
                print("w[%d][%d]= %s"%((i+1),(n_start + j+1),w[k]))
        k=k+1
    
    for i in range(0,n_in):
        for j in range(0,n_end):
            w[k]=w[k]+(l*error[j]*o[i+n_start])
            if m<it:
                print("w[%d][%d]= %s"%((i+n_start+1),(n_start + n_in + j+1),w[k]))
            k=k+1
    
#new theta value
    print("\nNEW BIAS : \n") 
    for i in range(0,(n_in+n_end)):
        tt=l*error[n_in+n_end-i-1]
        q[i]=q[i]+float(tt)
        if(m<it):
            print("q[%d]= %s"%((i+n_start+1),q[i]))
				






    
