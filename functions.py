'''
def sq_root(i):
    result = i * i
    return result


def product(i, j):
    result =  i / j
    return result


def prod_sum(i, j):
    prd = i * j
    sum_inp = i + j
    diff = i - j
    return prd, sum_inp, diff

def summary(i, j=0):
    print i, j
    print sq_root(i), sq_root(j)
    print product(i, j)
    print prod_sum(i, j)

# print sq_root(7)
# print product( 3, 5)
#a, b, c = prod_sum(3, 5)
#print a, b, c

#summary(5)


percen = lambda i, j: i / float(j) * 100

#print prod_func(47, 5)
print percen(50, 100)
print percen(60, 100)
'''


'''
def product_sum(i,j):
    prod = i * j
    sum_input = i + j
    diff = i - j
    return prod, sum_input, diff


a, b, c = product_sum(3,5)
#print a, b, c
'''


a = [1, 2, 5]
b = [1, 4, 5]

def check_list(a, b):
    for (x,y) in zip(a,b):
        if x == y:
            pass
        else:
            return False
    return True
print check_list(a, b)
