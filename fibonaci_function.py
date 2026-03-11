def fibo(n1):
    i=0
    n=0
    a=0
    b=1
    while(i<n1):
        print(n)
        n=a+b
        a=b
        b=n
        i+=1
    return "while loop completed"
    

n1=int(input("enter a number"))
temp=n1
print(fibo(n1))




































'''
def fibb(n1):
    series=[]
    a,b=0,1
    for i in range (n1):
        series.append(a)
        a,b=b, a+b
    
    return series

n1=10
print (fibb(n1))
'''