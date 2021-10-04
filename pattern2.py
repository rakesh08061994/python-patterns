num = int(input("Enter Number : "))
count = num
for i in range(1,num+1,2):
    print(count * " ", i * "0")
    count -= 1

'''
Enter Number : 10
           0    
          000   
         00000  
        0000000 
       000000000
'''