def padding(x):
    l=len(x)
    n=1
    while n<l:
        n*=2
        if n==l:
            return x
    return '0'*(n-l)+x

def karatsuba(x,y):
    n=len(x)
    print('n=',n)
    #print(n)
    if n==1:
        s= str(int(x)*int(y))
        #print(s)
        return s
    else:
        #x='0'*(max(len(x),len(y))-min(len(x),len(y)))+padding(x)
        #y='0'*(max(len(x),len(y))-min(len(x),len(y)))+padding(y)
        x=padding(x)
        y=padding(y)
        if len(x)>len(y):
            y='0'*(len(x)-len(y))+y
        elif len(y)>len(x):
            x='0'*(len(y)-len(x))+x
        n=len(x)
        n1=int(n/2)
        x1=x[0:n1]
        print('x1=',x1)
        x0=x[n1:n]
        print('x0=',x0)
        y1=y[0:n1]
        y0=y[n1:n]
        print('y1=',y1)
        print('y0=',y0)
        p1=karatsuba(x1,y1)
        #print('p1=',p1)
        p2=karatsuba(str(int(x1)+int(x0)),str(int(y0)+int(y1)))
        #print('p2=',p2)
        p3=karatsuba(x0,y0)
        p2=str(int(p2)-int(p1)-int(p3))
        p1=p1+'0'*n
        p2=p2+'0'*n1
        #print('p3=',p3)
        return str(int(p1)+int(p2)+int(p3))



#lenght of x and y is power of 10
#x='3141592653589793238462643383279502884197169399375105820974944592'
#y='3141592653589793238462643383279502884197169399375105820974944592'
x='3141592653589793238462643383279502884197169399375105820974944592'
y='2718281828459045235360287471352662497757247093699959574966967627'
print(karatsuba(x,y))
