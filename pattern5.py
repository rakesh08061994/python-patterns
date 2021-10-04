num = int(input("Enter Number : "))

count = num
for i in range(1,num+1):
    if  i%2 == 1:
        flag = True
    else:
        flag = False

    if flag:
        print(count * " ", i * "*")
    else:
        print(count * " ", (i-1) * "0")
        count -= 1


'''
Enter Number : 20
                     *
                     0
                    ***        
                    000        
                   *****       
                   00000       
                  *******      
                  0000000      
                 *********     
                 000000000     
                ***********    
                00000000000    
               *************   
               0000000000000   
              ***************  
              000000000000000  
             ***************** 
             00000000000000000 
            *******************
            0000000000000000000
'''