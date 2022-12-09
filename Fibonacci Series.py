x=int(input("n:"))
f1=0
f2=1
i=0
s=0
print(f1)
print(f2)
next=f1+f2
while(next <= x):
    if(i%2==0):
        s=s+next

    i=i+1
    print(next)
    f1=f2
    f2=next
    next=f1+f2
print("Sum:",s)
