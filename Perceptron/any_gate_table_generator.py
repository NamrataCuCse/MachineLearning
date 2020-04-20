#This program generates a truth table for any n input gate
from n_bit_binary_equivalent import bin
def gate_generator(no_of_inputs,gate_info,bipolar):
    inputs_list=[]
    for i in range(0,2**no_of_inputs):
        inputs_list.append(bin(i,no_of_inputs))

##    for i in range(0,2**no_of_inputs):
##        print(inputs_list[i])

    if gate_info==1:
        #AND Gate-- 
        for i in range(0,2**no_of_inputs):
            t=inputs_list[i][0]
            for j in range(1,no_of_inputs):
                t=t*inputs_list[i][j]
            inputs_list[i].append(t)    

    elif gate_info==2:
        #XOR Gate-- O/P=1 if no. of 1s in input is odd
        for i in range(0,2**no_of_inputs):
            count_of_1=0
            for j in range(0,no_of_inputs):
                if inputs_list[i][j]==1:
                    count_of_1=count_of_1+1
            if count_of_1%2==1:        
                inputs_list[i].append(1)
            else:
                inputs_list[i].append(0)
    elif gate_info==3:
        #NAND Gate-- O/P=0 only if all inputs are 1
        for i in range(0,2**no_of_inputs):
            count_of_1=0
            for j in range(0,no_of_inputs):
                if inputs_list[i][j]==1:
                    count_of_1=count_of_1+1
            if count_of_1==no_of_inputs:        
                inputs_list[i].append(0)
            else:
                inputs_list[i].append(1)        
    elif gate_info==4:
        #NOR Gate-- O/P=1 only if all inputs are 0s
        for i in range(0,2**no_of_inputs):
            count_of_0=0
            for j in range(0,no_of_inputs):
                if inputs_list[i][j]==0:
                    count_of_0=count_of_0+1
            if count_of_0==no_of_inputs:        
                inputs_list[i].append(1)
            else:
                inputs_list[i].append(0)
    else:
        print("Wrong choice")

    
    #Convert to bipolar form
    if bipolar:
        for i in range(0,2**no_of_inputs):
            for j in range(0,len(inputs_list[0])):
                if inputs_list[i][j]==0:
                    inputs_list[i][j]=-1

##    print("After appending t: ")
##    print()
##
##    for i in range(0,2**no_of_inputs):
##        print(inputs_list[i])
    return inputs_list
