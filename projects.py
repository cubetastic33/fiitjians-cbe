#HCF and LCM

steps = []

def euclids_algorithm(x, y):
    global steps
    steps = []
    return find_hcf(x, y)

def find_hcf(x, y):
    values = sorted([x, y], reverse=True)
    q = int(values[0] / values[1])
    r = values[0] % values[1]
    steps.append(str(values[0]) + ' = ' + str(values[1]) + ' x ' + str(q) + ' + ' + str(r))
    if r != 0:
        return find_hcf(values[1], r)
    return values[1], steps

def find_lcm(x, y):
    hcf = find_hcf(x, y)[0]
    return (x * y) / hcf

def find_factors(x):
    all_factors=[]
    n = 1
    while (n <= x):
        if x % n == 0:
            #n is a factor of x
            all_factors.append(n)
        n += 1
    return all_factors

def find_prime_factors(numberfortheparentforprimes, primefactors=[]):
    i = 2
    while (i <= numberfortheparentforprimes):
        parent = 0
        if (numberfortheparentforprimes % i == 0):
            parent = numberfortheparentforprimes/i
            primefactors.append(i)
            break
        i = i + 1      
    if (parent != 1):
        find_prime_factors(parent, primefactors)
        return primefactors
    else:    
        return primefactors
