import random
count=1
#Οριζόντιες και κάθετες
ori_kath= [0,1]
#Διαγωνίους
diagwnioi=[0,1]
m=50
o_k= ori_kath*5
d=diagwnioi*5
random.shuffle(o_k)
for i in range(m):
    print(o_k)
else:
    random.shuffle(d)
for j in range(m):
    print(d)
average=100/count
print(average)
