def Fibonacci_Fn(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (Fibonacci_Fn(n-1)+Fibonacci_Fn(n-2))
    
n=int(input("Enter the no. of terms"))
print("The fibonacci series is")

#print("Fib 0",Fibonacci_Fn(0))
for i in range(n):
    fib=Fibonacci_Fn(i)
    print(fib,end='\t')