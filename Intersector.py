#code to find the point of intersection of two line
#Intented to helo me with my assignments

def calparam(p1,p2):
        x1=p1[0]
        x2=p2[0]
        y1=p1[1]
        y2=p2[1]
        dinum=(x2-x1)
        if dinum==0:
            dinum=0.00001
        m=(y2-y1)/dinum
        c=y1-(m*x1)
        return m,c
def intersect(p1,p2,p3,p4):
        m1,c1=calparam(p1,p2)
        m2,c2=calparam(p3,p4)
        g=(m2-m1)
        if g==0:
            g=0.00001
        x=(c1-c2)/g
        y=(m1*x)+c1
        ans=[x,y]
        return ans
def callength(p1,p2):
    x=abs(p1[0]-p2[0])
    y=abs(p1[1]-p2[1])
    ans=(x**2+y**2)**0.5
    return ans
print(intersect([5,16],[43,32],[7,4],[45,17]))
print(callength([-165,-60.5],[7,4]))
