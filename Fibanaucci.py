n=int(input('ENTER A SERIES'))
f=0
s=1
print('fibanaucci series')
print(f,'/n',s)
for i in range(3,n+1):
 t=f+s
 print(t)
 f=s
 s=t
 
