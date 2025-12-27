str=input('ENTER A STRING')
lg=len(str)
mid=int(lg/2)
r=-1
for i in range(mid):
    if str[i]==str[r]:
     r=r-1
    else:
        print('NOT A PALINDROME')
else:
    print('IS A PALINDROME')
