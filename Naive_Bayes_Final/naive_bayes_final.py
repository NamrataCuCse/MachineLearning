#This program takes as input the total_table generated by the bayes_auto_gen program & classifies all the tuples not present in the main_table
#of this program

from math import log
from bayes_auto_gen import autogen_table

##Checks if the current tuple already exists in the main_table.
def checkValueExistance(array,table):
    for i in range(0,len(table)):
        count=0
        for j in range(0,len(array)):
            if(table[i][j]==array[j] ):
                count+=1
        if(count==4):
            return False    #Return False if exists

    return True             #Return true if not found

total_table=autogen_table() #store the all possible combination of attribute values without the class labels
print("The total list is: ")
print()
for i in range(0,len(total_table)):
    print(total_table[i])
print()

print()
print()
print()
no_of_attributes = 5
no_of_samples = 14
#main_table is the given training set
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
print("The given training database is: ")
for i in range(0,no_of_samples):
    print(main_table[i])
print()
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
print("Samples with count is: ",samples_with_count)
print()

#Calculate the Entropy(E) for individual attribute

gain = {}
attributes_with_count = {}
for i in range(0, col):
    sampleAttributes = []
    for j in range(0, no_of_samples):
        sampleAttributes.append(main_table[j][i])
    uniqueAttributes = set(sampleAttributes)    
    E = 0
    for k in uniqueAttributes:
        total,play_yes = 0,0
        for l in range(0,no_of_samples):
            if main_table[l][i] == k:
                total +=1
                if main_table[l][col] == 'Yes':
                    play_yes +=1
        
        attributes_with_count[k]={'yes' : play_yes, 'no': total - play_yes}
        
print("Attributes with count is: ",attributes_with_count)
print()

#New tuple classification
for m in range(0,len(total_table)):
    flag=True
    inputArray=total_table[m].copy()    #Store current tuple from the total_table
    while(flag):
        Outlook = inputArray[0]
        Temperature = inputArray[1]
        Humidity = inputArray[2]
        Windy = inputArray[3]
        if Outlook and Temperature and Humidity and Windy in attributes_with_count: #If all the given values are valid
            print()
            print()
            print("The current tuple is: ",inputArray)
            if(checkValueExistance(inputArray,main_table)):#Check if the current tuple already exists in the main_table
                print()
                pro_Yes,pro_No=1,1
                for i in range(len(inputArray)):
                    a=(attributes_with_count[inputArray[i]]['yes']/samples_with_count['Yes']['value'])  #Probability of attribute "i" for class YES
                    b=(attributes_with_count[inputArray[i]]['no']/samples_with_count['No']['value'])    #Probability of attribute "i" for class YES
                    print(attributes_with_count[inputArray[i]]['yes'],samples_with_count['Yes']['value'])
                    print(attributes_with_count[inputArray[i]]['no'],samples_with_count['No']['value'])
                    if(a!=0):
                        pro_Yes*=a  #product of all P(Xi|YES) for all i
                    if(b!=0):
                        pro_No*=b   ##product of all P(Xi|NO) for all i
                pro_Yes*=(samples_with_count['Yes']['value']/(samples_with_count['Yes']['value']+samples_with_count['No']['value']))    #P(X|YES)*P(YES)
                pro_No*=(samples_with_count['No']['value']/(samples_with_count['Yes']['value']+samples_with_count['No']['value']))      #P(X|NO)*P(NO)

                if(pro_Yes>pro_No):
                    print("possible to play")
                    inputArray.append('Yes')
                    main_table.append(inputArray)
                else:
                    print("not possible to play")
                    inputArray.append('No')
                    main_table.append(inputArray)
            else:
                print("Entry already exists!")
            flag=False

print()
print("After adding class labels the final main_table is: ")
print()
for i in range(len(main_table)):
    print(main_table[i])

