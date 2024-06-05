def odd(n):
    return n % 2 == 1
lst=list(filter(odd, range(10)))
print(lst)