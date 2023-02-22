import time
def change(r,c,t,sym,end):
    if(t[r][c]!="X" and t[r][c]!="O"):
        t[r][c]=sym
        print("\n")
        print(t[0])
        print(t[1])
        print(t[2])
    else:
        print("You can't fill in this location... Because that location is already filled by",t[r][c],"symbol\nYou had lost your chance...")
        end+=1
    return end
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
t=[["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]]
p1=input("enter player-1 name:")
p2=input("enter player-2 name:")
print("By default all the position on the board is filled with the \"_\" ")
time.sleep(2)
print("welcome",p1,"and",p2)
print("Let's start the game....\n\n")
time.sleep(2)
print(t[0])
print(t[1])
print(t[2])
i=0
end=9
while(1):
    if(i%2==0):
        print(p1,"enter coordinates:")
        r=int(input("row:"))
        c=int(input("column:"))
        sym="X"
        end=change(r,c,t,sym,end)
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
        end=change(r,c,t,sym,end)
        res=check(sym)
        if(res==1):
            print(p2,"won")
            break
        else:
            m=input("do you want to continue y/n ?")
            if(m=="n"):
                break
    if(i==end):
        print("nobody won")
        break
    i+=1
