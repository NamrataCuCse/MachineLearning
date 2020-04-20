
from any_gate_table_generator import gate_generator
                                            #decimal number
def learn(inputs_list,weights,iteration,no_of_inputs,theta,eta):
    
    rows=len(inputs_list)
    columns=len(inputs_list[0])-1
    calc_table=[]
    for x in range(0,rows):
        y_in=0
        t=inputs_list[x][no_of_inputs+1]
        temp_list=inputs_list[x].copy()#Copy current list to temporary list "temp_list"

        for z in range(0,columns):
            y_in=(temp_list[z]*weights[z])+y_in
        if y_in>theta:
            y_out=1
        elif -theta<=y_in and y_in<=theta:
            y_out=0
        elif y_in<-theta:
            y_out=-1
        temp_list.append(y_in)
        temp_list.append(y_out)

        if y_out!=t:
            for k in range(0,columns):
                weights[k]=weights[k]+(eta*t*temp_list[k])

        temp_list.extend(weights)
        calc_table.append(temp_list)
        temp_list=[]
        
    #calc_table format: x0,x1,x2,x3,....t,y_in,y_out,w0,w1,w2,w3....
    print("The final calculation table after Iteration",iteration,"is:")    
    for x in range(0,rows):
        print(calc_table[x])
    return calc_table    

#This function checks whether the convergence criteria is satisfied        
def check(temp_table,no_of_inputs):
    flag=True
    for i in range(0,len(temp_table)):
        if temp_table[i][no_of_inputs+1]!=temp_table[i][no_of_inputs+3]:
            flag=False
            break;
    return flag    

def perceptron_main(gate_info,no_of_inputs,eta):
    #Main Program#

    #initialize weight matrix
    weights=[]
    for i in range(0,no_of_inputs+1):
        weights.append(0)

    #Initialize other parameters

    theta=1
    iteration=1
    t_value=False

    #Generate truth table with target class value
    inputs_list=gate_generator(no_of_inputs,gate_info,True)

    print("The given training set is: ")
    for i in range(0,2**no_of_inputs):
        print(inputs_list[i])
    print()
    print()
    #Append x0
    for i in range(0,2**no_of_inputs):
        inputs_list[i].insert(0,1)

    while not t_value:
        main_table=learn(inputs_list,weights,iteration,no_of_inputs,theta,eta)
        t_value=check(main_table,no_of_inputs)
        if not t_value:
            weights=main_table[(2**no_of_inputs)-1]
            weights=weights[no_of_inputs+4:]
            print()
            print()
            print("The new weights are: ",weights)
            print("-------------------------------------------------------------------------------------------------")
            print()
            iteration=iteration+1

    weights=main_table[(2**no_of_inputs)-1]
    weights=weights[no_of_inputs+4:]
    print("-------------------------------------------------------------------------------------------------")
    print()
    print("The solution is: ",weights)        
    return iteration
