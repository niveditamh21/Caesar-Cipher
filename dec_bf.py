#Brute Force Attack to decrypt a Cipher Text
ns=input()
o=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for k in range(1,26):
        s=[]
        st=''
        for i in range(k,26):
                s.append(o[i])
        for i in range(0,k):
                s.append(o[i])
        for i in ns:
                if(i.isalpha()==True):
                       ind=s.index(i)
                       st+=o[ind]
                else:
                       st+=i
         print(st)
