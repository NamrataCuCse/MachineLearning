#This program generates the following table:


##['Sunny', 'Hot', 'High', 'True']
##['Sunny', 'Hot', 'High', 'False']
##['Sunny', 'Hot', 'Normal', 'True']
##['Sunny', 'Hot', 'Normal', 'False']
##['Sunny', 'Mild', 'High', 'True']
##['Sunny', 'Mild', 'High', 'False']
##['Sunny', 'Mild', 'Normal', 'True']
##['Sunny', 'Mild', 'Normal', 'False']
##['Sunny', 'Cold', 'High', 'True']
##['Sunny', 'Cold', 'High', 'False']
##['Sunny', 'Cold', 'Normal', 'True']
##['Sunny', 'Cold', 'Normal', 'False']
##['Rainy', 'Hot', 'High', 'True']
##['Rainy', 'Hot', 'High', 'False']
##['Rainy', 'Hot', 'Normal', 'True']
##['Rainy', 'Hot', 'Normal', 'False']
##['Rainy', 'Mild', 'High', 'True']
##['Rainy', 'Mild', 'High', 'False']
##['Rainy', 'Mild', 'Normal', 'True']
##['Rainy', 'Mild', 'Normal', 'False']
##['Rainy', 'Cold', 'High', 'True']
##['Rainy', 'Cold', 'High', 'False']
##['Rainy', 'Cold', 'Normal', 'True']
##['Rainy', 'Cold', 'Normal', 'False']
##['Overcast', 'Hot', 'High', 'True']
##['Overcast', 'Hot', 'High', 'False']
##['Overcast', 'Hot', 'Normal', 'True']
##['Overcast', 'Hot', 'Normal', 'False']
##['Overcast', 'Mild', 'High', 'True']
##['Overcast', 'Mild', 'High', 'False']
##['Overcast', 'Mild', 'Normal', 'True']
##['Overcast', 'Mild', 'Normal', 'False']
##['Overcast', 'Cold', 'High', 'True']
##['Overcast', 'Cold', 'High', 'False']
##['Overcast', 'Cold', 'Normal', 'True']
##['Overcast', 'Cold', 'Normal', 'False']


def autogen_table():
    Outlook=['Sunny','Rainy','Overcast']
    Temperature=['Hot','Mild','Cold']
    Humidity=['High','Normal']
    Windy=['True','False']
    total_list=[]
    total_list2=[]
    temp_list=[]
    temp_list2=[]
    for i in range(0,3):
        for j in range(0,3):
            temp_list.append(Outlook[i])
            temp_list.append(Temperature[j])
            total_list.append(temp_list)
            temp_list=[]


    for i in range(0,len(total_list)):
        for j in range(0,2):
                temp_list=total_list[i].copy()
                temp_list.append(Humidity[j])
                total_list2.append(temp_list)
                
                
    total_list.clear()
    for i in range(0,len(total_list2)):
        for j in range(0,2):
                temp_list=total_list2[i].copy()
                temp_list.append(Windy[j])
                total_list.append(temp_list)
                

    return total_list
