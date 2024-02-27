
def fibonacci_loop():
    prev2 = 0
    prev1 = 1

    print(prev2)
    print(prev1)
    for fibo in range(18):
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo


# fibonacci_recursion
def fibonacci_recursion(n_rounds):
    print(0)
    print(1)
    prev_n = 0
    curr_n = 1
    count = 2
    final_list = []

    def inner_function(n_rounds, prev_n, curr_n, count, final_list):
        if count <= n_rounds:
            newFibo = prev_n + curr_n
            print(newFibo)
            final_list.append(newFibo)
            prev_n = curr_n
            curr_n = newFibo
            count += 1
            return inner_function(n_rounds, prev_n, curr_n, count, final_list)
        else:
            return final_list
        
    return inner_function(n_rounds, prev_n, curr_n, count, final_list)

result = fibonacci_recursion(15)
print(result)  



# Nth	Fibonacci number	Total
# 1	0	
# 2	1	1
# 3	1	2
# 4	2	3
# 5	3	5
# 6	5	8
# 7	8	13
# 8	13	21
# 9	21	34
# 10	34	55
# 11	55	89
# 12	89	144
# 13	144	233
# 14	233	377
# 15	377	610