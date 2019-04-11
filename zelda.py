import random
a=random.randint(1,100)
while(1):
    b=input('请输入：')
    b=int(b)
    if (a<b):
        print("big")
    if(a>b):
        print('small')
    if(a==b):
        print('yes')
        break
