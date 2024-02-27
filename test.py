# def fibo(n):    
#     if n == 3 or n == 2:
#         return 1;
#     elif n <= 1: 
#         return 0;
#     else:
#         return (fibo(n - 1) + fibo(n - 2))
    
# for i in range(10):
#     print(f"F{i+1}: {fibo(i+1)}")


def fibo(n, flist = [0, 1]):
    flist_qty = len(flist)
    if n == 1: 
        return 0
    elif n == 2: 
        return 1
    elif n == flist_qty + 1:
        new_fibon_no = flist[n-1-1] + flist[n-2-1]
        return new_fibon_no
    else:
        flist.append(flist[n-n-1-1] + flist[n-n-1-1])
        return fibo(n)
print(fibo(5))