import random
count=1
ori_kath= [0,1]
diagwnioi=[0,1]
m=50
#Οριζόντιες και κάθετες
list1= ori_kath*5
#Διαγωνιοι
list2=diagwnioi*5
random.shuffle(list1)
for i in range(m):
    print(list1)
else:
    random.shuffle(list2)
for j in range(m):
    print(list2)
average=100/count
print(average)