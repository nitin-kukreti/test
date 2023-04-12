'''
 Author : Nitin KuKreti

 taking list input from user which is seprated by space
 ex 5 4 6 7 
 which will converted as [5,4,6,7]
 after processing

'''

data= input("enter list numbers which are sepreated by space ex:5 6 7 \n").split()


 
# preprocessing 

processData=[int(x) for x in data]

# creating new list of even nuber for processed list

evenList=[x for x in processData if x%2==0]




#  output stuff


print('processlist',processData)

print(("evenlist",evenList))

print("sum of process list",sum(processData))

print("sum of even list",sum(evenList))







