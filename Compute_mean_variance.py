# compute mean and variance manually python
def mean_c(n):
    if not n:
        return 0
    sum_n = sum(n)
    return sum_n/len(n)

def variance_c(n):
    length = len(n)
    if length<2:
        return 0
    sum_c = 0.0
    mean_n = sum(n)/length
    sum_c = sum((x-mean_n)**2 for x in n)
    
    return sum_c/(length-1)

n = [1,2,3]
mean_c(n)
variance_c(n)
