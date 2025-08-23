def flatten(lst):
    new_list = []
    for item in lst:
        if type(item) == list:
            for i in item:
                if type(i) == list:
                    for j in i:
                        new_list.append(j)
                else:
                    new_list.append(i)
        else:
            new_list.append(item)
    return new_list
# Input:
data = [[1,'a',['cat'],2],[[3]],'dog',4,5]
print(flatten(data))
# Output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]


def reverse_nested(lst):
    new_list = []
    for i in range(len(lst)-1, -1, -1):   # dış listeyi sondan başa al
        if isinstance(lst[i], list):      # eğer eleman da listeyse
            inner = []
            for j in range(len(lst[i])-1, -1, -1):  # iç listeyi de tersine al
                inner.append(lst[i][j])
            new_list.append(inner)
        else:
            new_list.append(lst[i])
    return new_list
# Input:
data = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_nested(data))
# Output: [[7, 6, 5], [4, 3], [2, 1]]