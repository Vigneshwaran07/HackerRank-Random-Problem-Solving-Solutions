n,k = map(int,input().strip().split())
c=list(map(int,input().strip().split()))[::k]
print(100-sum([i+(i==1)+1 for i in c]))
