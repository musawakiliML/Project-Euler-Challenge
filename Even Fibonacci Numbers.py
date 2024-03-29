'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''


def Fibonacci_even_valued_terms(n):

    f = [0, 1]
    even_values = 0 


    for i in range(2, n+1):
        #f.append(f[i-1] + f[i-2])
        if (f(i-1) + f(i-2)) % 2 == 0:
            even_values = even_values + (f(i-1) + f(i-2))
    return even_values
print(Fibonacci_even_valued_terms(20))

'''
def Fibonacci_even(n):
    even_values = 0

    if n < 0:
        print("Invalid input!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        j = 0
        while j < n:
            #if (Fibonacci_even(i-1) + Fibonacci_even(i-2)) % 2 == 0:
                #even_values = even_values + (Fibonacci_even(i-1) + Fibonacci_even(i-2))
            (Fibonacci_even(n-1) + Fibonacci_even(n-2)
            j += 1

Fibonacci_even(10)
'''
