#IMPLEMENTATION OF BANKERS ALGORITHM IN PYTHON
a = int(input("the number of processes:  "))
b = int(input("the number of resources:  "))
c = int(input("the number of  instances:  ")) 
d = int(input("the number of resources in an instances:  "))
#now List
print("Total number of process: ")
i = 1
for i in range(1,a):
    print(i)
    i = i+1
print("Total number of resources are: ")
j = 1
for j in range (1,b):
    print(j)
    j = j+1
#list for process
process = [1,2,3,4,5]
print("Process :") 
print(process)
#list for resources
res = [1,2,3,4,5]
print("Resources: " )
print(res)
#instances of per resources = 2
print("Instances with respect to resource allocation: ")
res1 = 2
res2 = 2
res3 = 2
res4 = 2
res5 = 2
ins = [2,2,2,2,2]
obj1 = enumerate(ins)
print(list(enumerate(ins,1)))
#now Allocation and request can we wriiten according to processes
print("Resources that are allocated to the process")
ress = [1,2,3,4,5]
print(ress,ins)
print("Resource requested to the process")
resss = [1,2,3,4,5]
q1 =int(input("Enter the process 1 request : "))
q2 =int(input("Enter the process 2 request : "))
q3 =int(input("Enter the process 3 request : "))
q4 =int(input("Enter the process 4 request : "))
q5 =int(input("Enter the process 5 request : "))
print(((q1,q2,q3,q4,q5),ress))