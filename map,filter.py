# l=[1,2,3,4,5,6]
# print(*list(map((lambda x:x**2),l)),sep='\n')
# def cube(x):
#     return x**3
# l=[1,2,3,4,5,6]
# newl=list(map(cube,l))
# print(*newl)
# newll=list(filter(lambda x:x>4,l))
# print(newll)

# n=input("enter para:")
# l=n.split('r')
# print(*l)
from functools import reduce
l=[1,2,3,4,5,6]
newl=reduce((lambda x,y:x+y),l)
print(newl)