def bin(number,no_of_bits):
#number=int(input("Enter the number:"))
#dup=number
#no_of_bits=int(input("Enter the number of bits"))
    list=[]
    if number==0:
        for i in range(0,no_of_bits):
            list.append(0)
    else:
        while number!=0:
            remainder=number%2
            list.append(remainder)
            number=int(number/2)
        for i in range(0,no_of_bits-len(list)):
            list.append(0)
        list.reverse()
#print("The binary equivalent of",dup,"is",list)
    return list    
