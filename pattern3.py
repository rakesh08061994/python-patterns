num = int(input("Enter Number : "))

count = 1
list1 = []
for i in range(1,num+1,2):
    list1.append(i)
list1.sort(reverse=True)

for i in list1:
    print(count * " ",i * "0")
    count += 1
    
'''
Enter Number : 10
  000000000
   0000000 
    00000  
     000   
      0    
'''
