#Frequency Analysis Attack to decrypt a Cipher Text
ct=input()
o=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
d={}
for i in ct:
      if i in d:
           d[i]+=1
      else:
          d[i]=1
pr='NO'
while(pr=='NO'):
      while True:
          ma=max(d,key=d.get)
          if(ma.isalpha()==True):
                break
          else:
                del d[ma]
      k=o.index(ma)-o.index('E')
      s=[]
      for i in range(k,26):
          s.append(o[i])
      for i in range(0,k):
          s.append(o[i])
      st=''
      for i in ct:
          if(i.isalpha()==True):
                x=s.index(i)
                st+=o[x]
          else:
                st+=i
      print(st)
      pr=input("Are you satisfied: YES/NO ?\n")
      if(pr=='YES'):
          print("YOU HAVE SUCCESSFULLY HACKED í¸ˆ")
          break
      else:
          del d[ma]
          continue
