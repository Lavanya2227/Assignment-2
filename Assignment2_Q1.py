""" list = []
line = input("Enter the list of touples:" )
list.append(tuple(line.split()))
for i,j in range (0 ,1):
    if 0 > 1:
       print(sorted(list)) """


def last(n) : return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))






       












