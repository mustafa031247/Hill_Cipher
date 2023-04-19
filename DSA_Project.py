#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def build_matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
def index_finder(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(main_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def Ciphering():  #Encryption
    msg=str(input("Enter Message:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=index_finder(msg[i])
        loc1=list()
        loc1=index_finder(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(main_matrix[(loc[0]+1)%5][loc[1]],main_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(main_matrix[loc[0]][(loc[1]+1)%5],main_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(main_matrix[loc[0]][loc1[1]],main_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def Deciphering():  #Decipheringion
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=index_finder(msg[i])
        loc1=list()
        loc1=index_finder(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(main_matrix[(loc[0]-1)%5][loc[1]],main_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(main_matrix[loc[0]][(loc[1]-1)%5],main_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(main_matrix[loc[0]][loc1[1]],main_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        


main_key=input("Enter KEY")
main_key=main_key.replace(" ", "")
main_key=main_key.upper()
Result_list=list()

for c in main_key: #storing main_key
    if c not in Result_list:
        if c=='J':
            Result_list.append('I')
        else:
            Result_list.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in Result_list:
        if i==73 and chr(74) not in Result_list:
            Result_list.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            Result_list.append(chr(i))
k=0
main_matrix=build_matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        main_matrix[i][j]=Result_list[k]
        k+=1

while(flag):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    flag = True
    if choice==1:
        Ciphering()
    elif choice==2:
        Deciphering()
    elif choice==3:
        flag = False
    else:
        print("Choose correct choice")

