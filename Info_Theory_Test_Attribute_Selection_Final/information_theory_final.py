#This program identifies the attribute with the highest GAIN value

from math import log

##main_table=[]
##temp_list=[]
##no_of_attributes=int(input("Enter the total number of attributes(including the class_label attribute):"))
##no_of_samples=int(input("Enter the total number of samples in the database:"))
####no_of_classes=2
#Populate the database
##for i in range(0,no_of_samples):
##    print("Sample ",i+1)
##    for j in range(0,no_of_attributes):
##        print("Attribute ",j+1)
##        x=input()
##        temp_list.append(x)
##    main_table.append(temp_list)
##    temp_list=[]

no_of_attributes = 5
no_of_samples = 14
main_table = [['Sunny', 'Hot', 'High', 'False', 'No'],
['Sunny', 'Hot', 'High', 'True', 'No'],
['Overcast', 'Hot', 'High', 'False', 'Yes'],
['Rainy', 'Mild', 'High', 'False', 'Yes'],
['Rainy', 'Cold', 'Normal', 'False', 'Yes'],
['Rainy', 'Cold', 'Normal', 'True', 'No'],
['Overcast', 'Cold', 'Normal', 'True', 'Yes'],
['Sunny', 'Mild', 'High', 'False', 'No'],
['Sunny', 'Cold', 'Normal', 'False', 'Yes'],
['Rainy', 'Mild', 'Normal', 'False', 'Yes'],
['Sunny', 'Mild', 'Normal', 'True', 'Yes'],
['Overcast', 'Mild', 'High', 'True', 'Yes'],
['Overcast', 'Hot', 'Normal', 'False', 'Yes'],
['Rainy', 'Mild', 'High', 'True', 'No']
]

#Print the database
for i in range(0,no_of_samples):
    print(main_table[i])

col = no_of_attributes - 1

#Calculate the Entropy(I) to classify a given sample
sampleClass = []
for i in range(0,no_of_samples):
    sampleClass.append(main_table[i][col])

uniqueClass = set(sampleClass)
samples_with_count = {}

for i in uniqueClass:
    samples_with_count[i] = { 'value' : sampleClass.count(i), 'probablity' : sampleClass.count(i) / no_of_samples }

##keys list
keyList = []
for key in samples_with_count.keys():
  keyList.append(key)
  
uniqueClassCount = len(samples_with_count)
print(samples_with_count)
sum = 0

for i in samples_with_count:
    log_val=log(samples_with_count[i]['probablity'],2)
    a = -(samples_with_count[i]['probablity'] * log_val)
    sum += a

print(sum)

#Calculate the Entropy(E) for individual attribute

def test(total,yes):
    no=total-yes
    temp = 0
    if(total!=yes):
        a=log((yes/total),2)
        temp += (yes/total)*a
        b=log((no/total),2)
        temp += (no/total)*b
    return(-temp)

gain = {}
for i in range(0, col):
    sampleAttributes = []
    for j in range(0, no_of_samples):
        sampleAttributes.append(main_table[j][i])
    uniqueAttributes = set(sampleAttributes)

    print(uniqueAttributes)
    
    E = 0
    for k in uniqueAttributes:
        total,play_yes = 0,0
        for l in range(0,no_of_samples):
            if main_table[l][i] == k:
                total +=1
                if main_table[l][col] == keyList[0]:
                    play_yes +=1        
        print(k,total)
        tmp = test(total,play_yes)        
        E += (total/no_of_samples)*tmp
        print(tmp)
    gain[i] = sum - E
    print("Expectation =", E)
print("Gain:")
for i in range(0, col):
    print(gain[i])
maxGain = max(gain.values())
print("Max Gain:", maxGain)
for key in gain.keys():
  if gain[key] == maxGain:
    print("Selected attribute: Attribute[", key,"]")

##
##    print(samples_with_count)

