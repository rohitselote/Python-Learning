#reduce()
from functools import reduce
expenses = [("dinner",180),("car repair",120)]

# for expense in expenses:
#     sum+=expense[1]
# print(sum)   


sum=reduce(lambda a,b : a[1] + b[1] , expenses)
print(sum)
