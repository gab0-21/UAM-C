
def sumapares(n,m):
    i= 0
    while n<=m:
        if n%2==0:
            i= i+n
        else:
            i= i
        n= n+1
    return i


