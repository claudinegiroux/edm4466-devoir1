# encoding:utf-8

l1= list(range(20000,30151))
# print(l1)
n=0
url="https://montrealcampus.ca?p="
urlfinal=[]
# mc= url.replace("z","l1")
# print(mc)

for num in range(20000,30151):
    n+=1
    print(n,url+str(num))
    urlfinal.append(url+str(num))

print(urlfinal)
print(len(urlfinal))
