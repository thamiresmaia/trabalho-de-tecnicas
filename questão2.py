def crip(r):
    if(r<6):
        return r+4
    else:
        return r-6
num = input('digite o número de 4 digitos descriptografar: ')
a=0
if(len(num)!=4):
    while (a < 1):
        num = input('digite o número de 4 digitos para descriptografado novamente: ')
        a+=1
        if(len(num)!=4):
            a-=1;
    troca1 = [1,2,3,4]
    troca1[0]=num[2]
    troca1[1]=num[3]
    troca1[2]=num[0]
    troca1[3]=num[1]

    troca1[0]=(int(troca1[0])+6)%10
    troca1[1]=(int(troca1[1])+6)%10
    troca1[2]=(int(troca1[2])+6)%10
    troca1[3]=(int(troca1[3])+6)%10
else:
    troca1 = [1,2,3,4]
    troca1[0]=num[2]
    troca1[1]=num[3]
    troca1[2]=num[0]
    troca1[3]=num[1]

    troca1[0]=(int(troca1[0])+6)%10
    troca1[1]=(int(troca1[1])+6)%10
    troca1[2]=(int(troca1[2])+6)%10
    troca1[3]=(int(troca1[3])+6)%10
print(troca1)
num = input('digite o número de 4 digitos criptografado: ')
a = 0
if(len(num)!=4 ):
    while (a < 1):
        num = input('digite o número de 4 digitos criptografado novamente: ')
        a+=1
        if(len(num)!=4):
            a-=1;
    troca = [1,2,3,4]
    troca[0]=num[2]
    troca[1]=num[3]
    troca[2]=num[0]
    troca[3]=num[1]

    troca[0]=crip(int(troca[0]))
    troca[1]=crip(int(troca[1]))
    troca[2]=crip(int(troca[2]))
    troca[3]=crip(int(troca[3]))
else:
    troca = [1,2,3,4]
    troca[0]=num[2]
    troca[1]=num[3]
    troca[2]=num[0]
    troca[3]=num[1]

    troca[0]=crip(int(troca[0]))
    troca[1]=crip(int(troca[1]))
    troca[2]=crip(int(troca[2]))
    troca[3]=crip(int(troca[3]))
print(troca)
