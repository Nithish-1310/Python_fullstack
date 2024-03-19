def fact_recur(n):
    if n == 1:
        return n
    
    else:
        return n * fact_recur(n-1)

n =  int(input("Enter the number: "))

print(fact_recur(n))