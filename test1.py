import random
x=int(input('请输入随机数上限:'))
sum=0
count=0
while count<10:
    number=random.randint(0,x)
    print(number)
    sum=sum+number
    count=count+1
a=sum/10
print(a)