from functools import reduce

a = [1,2,3,4,5]
product = lambda x,y: x*y
result = reduce(product,a)
print(result)