#Now function for printing faboniccai series
def fec(n1,n2,n):
    if n==0:#conditon of termination
        return
    result=n1+n2
    print(result,end=' ')
    fec(n2,result,n-1)
#now main program for faboniccai 
a=0
b=1
n=int(input('How many numbers are to be printed   '))
print('The febonacci series is :-')
print(a,end=' ')
print(b,end=' ')
fec(a,b,n-2)