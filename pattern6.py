num = int(input("Enter Number : "))
count = num
for i in range(1,num+1):
    a = ((count+i) * "*")
    if i == int((num)/2):
        print("\n")
    else:
        print(a)
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
'''
