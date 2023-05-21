def random_value(seed, n, a, b, integer=True):
    # This function returns 'n' number of random values (int / float) between 'a' and 'b'. It bases its numbers on seed.
    if integer:
        for i in range(n):
            num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1))))) % 10**13)/10**13)
            print(num)
    else:
        for i in range(n):
            num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1))))) % 10**13)/10**13
            print(num)
    return num


print(random_value(37, 100, 0, 100, integer=True))
