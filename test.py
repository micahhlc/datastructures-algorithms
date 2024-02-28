def fibo(n, flist = [0, 1]):
    flist_qty = len(flist)
    if n <= 1: 
        return n
    elif n == flist_qty:
        new_fibon_no = flist[n-1] + flist[n-2]
        return new_fibon_no
    else:
        flist.append(flist[flist_qty - 1] + flist[flist_qty - 2])
        print(flist)
        return fibo(n)

for i in range(10):
    print(f"F{i+1}: {fibo(i)}")


