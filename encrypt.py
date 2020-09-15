#Caesar Cipher to encrypt a Plain Text
import random
st=input()
o=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s=[]
ns=''
k=random.randrange(1,26,1)
for i in range(k,26):
        s.append(o[i])
for i in range(0,k):
        s.append(o[i])
for i in st:
        if(i.isalpha()==True):
                 ind=o.index(i)
                 ns+=s[ind]
        else:
                 ns+=i
print(ns)
