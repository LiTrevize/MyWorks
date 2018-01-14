import math
def C(m,n):
    if m<n:
        return 1
    a=1
    b=1
    for i in range(n):
        a*=(m-i)
        b*=(i+1)
    return a//b
class course:
    def __init__(self,name="",limit=0,selected=0):
        self.name=name
        self.limit=limit
        self.selected=selected

    def probability(self,n=1,m=1):
        if m==n:
            return C(self.selected-n,self.limit-n)/C(self.selected,self.limit)
        elif m==0:
            return C(self.selected-n,self.limit)/C(self.selected,self.limit)
        elif m==-1:
            return 1-self.probability(n,0)

a=course("Japanese",40,92)
print(a.probability())
print(a.probability(2,2))
print(a.probability(2,-1))