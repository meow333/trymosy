r=raw_input();
s=r.split()
s1=""
for i in range(len(s)):
    if(i%2==0):
        s[i]=s[i][::-1]
        if "." in s[i]:
            s[i]=s[i].replace('.', '')
    #print s[i]
s1=s[0]
for i in range(1,len(s)):
    s1=s1+" "+s[i]
s1=s1+'.'
print s1
