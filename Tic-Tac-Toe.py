def change(r,w,t,sym):
    t[r][w]=sym
    print(t[0])
    print(t[1])
    print(t[2])
def check(sym):
    for i in range(3):
        if(t[i][0]==sym and t[i][1]==sym and t[i][2]==sym):
            return 1
        if(t[0][i]==sym and t[1][i]==sym and t[2][i]==sym):
            return 1
    if((t[0][0]==sym and t[1][1]==sym and t[2][2]==sym) or (t[0][2]==sym and t[1][1]==sym and t[2][0]==sym)):
        return 1
    else:
        return 0
t=[["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]]
p1=input("enter player-1 name:")
p2=input("enter player-2 name:")
print(t[0])
print(t[1])
print(t[2])
i=0
while(1):
    if(i%2==0):
        print(p1,"enter coordinates:")
        r=int(input("row:"))
        c=int(input("column:"))
        sym="*"
        change(r,c,t,sym)
        res=check(sym)
        if(res==1):
            print(p1,"won")
            break
        else:
            m=input("do you want to continue y/n ?")
            if(m=="n"):
                break
    else:
        print(p2,"enter coordinates:")
        r=int(input("row:"))
        c=int(input("column:"))
        sym="O"
        change(r,c,t,sym)
        res=check(sym)
        if(res==1):
            print(p2,"won")
            break
        else:
            m=input("do you want to continue y/n ?")
            if(m=="n"):
                break
    if(i==9):
        print("nobody won")
    i+=1