def fibonacci(n):
    series = [0, 1]  
    
    while len(series) < n:
        next_num = series[-1] + series[-2]  
        series.append(next_num)  
    
    return series

# Example usage
num_terms = 100
fib_series = fibonacci(num_terms)
print(fib_series)