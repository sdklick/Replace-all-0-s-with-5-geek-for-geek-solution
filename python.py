# replace all 0 with 5

s = [1004,121] # You will be write s=[n]
nes=[]

for i in s:
    data=""
    for j in str(i):
        if int(j)==0:
            data+="5"
        elif int(j)!=0:
            data+=j  
    nes.append(int(data))          
for x in nes:
    print(x)        

