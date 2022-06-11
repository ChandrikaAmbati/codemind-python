n=list(map(str,input().split()))
a=[]
b=[]
d=[]
for i in n:
    a.append(ord(min(i)))
    b.append(ord(max(i)))
s1=0
s2=0
for i in a:
    s1=s1+i
for i in b:
    s2=s2+i
print(abs(s1-s2))    

    