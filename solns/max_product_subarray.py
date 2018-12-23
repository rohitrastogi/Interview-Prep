def maximal_subarray_product(a):
    max_product = a[0]
    min_product = a[0]
    res = a[0]

    for i in range(1, len(a)):
        temp = max_product
        max_product = max(a[i], max_product * a[i], min_product * a[i])
        min_product = min(a[i], temp * a[i], min_product * a[i])

        if max_product > res:
            res = max_product
    
    print(max_product, min_product, res)
    return res 

test = [-2, -10, 5, -2, -900]
print(maximal_subarray_product(test))

