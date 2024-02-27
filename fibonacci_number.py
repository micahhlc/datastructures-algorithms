
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
            inner_function(n_rounds, prev_n, curr_n, count, final_list)
        else:
            return final_list
    return inner_function(n_rounds, prev_n, curr_n, count, final_list)

result = fibonacci_recursion(5)
print(result)  # Output will be 15





# fibonacci_loop()

#Python