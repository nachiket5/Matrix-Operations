import numpy as np
a = int(input())
ls = []
res =[]
for i in range(a):
    k = list(map(int,input().split()))
    ls.append(k)
for i in range(-(a-1),a):
    dg =list(np.array(ls).diagonal(i))
    if len(dg) >=4:
        res.append(dg)
# print(list(np.array(ls).shape))
ary=np.array(ls)
for i in ary:
    if len(i)>=4:
        res.append(list(i))

trans =np.array(ls).T
for i in  trans:
    if len(i) >=4:
        res.append(list(i))

# print(res)
result =[]
for i in res:
    nm =0
    for x in range(0,len(i)):
        a = i[nm:nm+4]
        if len(a)==4 and  str(a[0])==str(a[1]) and str(a[0])==str(a[2]) and str(a[0])==str(a[3]) and a not in result:
                result.append(a)
        nm +=1

if len(result) >=1:
    print(min(min(result)))
else:
    print(-1)





# result =[]
# for i in res:
#     for j in i:
#         n =i.count(j)
#         if n >=4:
#             result.append(j)
# if len(result) >=1:
#     print(min(result))
# else:
#     print(-1)


