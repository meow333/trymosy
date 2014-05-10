n=input()
ap=raw_input()
p=ap.split();
for i in range(n-2):
    d1=int(p[i+1])-int(p[i])
    d2=int(p[i+2])-int(p[i+1])
    if d2>d1:
        d=d1
    else:
        d=d2
print d
for j in range(n-1):
    dx=int(p[j+1])-int(p[j])
    if dx!=d:
        pos=j
        pp=int(p[j])
        break;
print pp+d
r=p[0]
for k in range(1,n):
    r=r+' '+p[k]
    if k==pos:
        r=r+' '+str((int(p[k])+d))
print r
