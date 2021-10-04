num = int(input("Enter Number : "))


count = num
for i in range(1,num+1):
    print((count+i) * "*")
    count -= 1

''' 
Enter Number : 10

***********
***********
***********
***********
***********
***********
***********
***********
***********
***********
'''
