from perceptron import perceptron_main
print("1.AND 2.XOR 3.NAND 4.NOR")
gate_info=int(input("Enter your choice: "))
print("2. 2-input  3. 3-input  4.4-input")
no_of_inputs=int(input("Enter your choice: "))
eta_low=float(input("Enter the lower range of learning rate: "))
eta_high=float(input("Enter the upper range of learning rate: "))
i=eta_low
iterations_list=[[],[]]
temp_list=[]
while i<=eta_high:
    print()
    print()
    print()
    print()
    print("For learning rate: ",i)
    print("---------------")
    print()
    iterations_list[0].append(perceptron_main(gate_info,no_of_inputs,i))
    iterations_list[1].append(i)
    i=i+0.01
print()
print()
print("The iterations_list is: ",iterations_list)
print()
print()
for i in range(0,len(iterations_list[0])):
    if min(iterations_list[0])==iterations_list[0][i]:
        print("The learning rate: ",iterations_list[1][i]," requires the smallest number of iterations, namely ",iterations_list[0][i]," iterations to converge.")
