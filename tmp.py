my_dict = {'0': ['A','B','C','D','E','F'],
           '1' : ['B','C'],
           '2' : ['A','B','D','E','G'],
           '3' : ['A','B','C','D','G'],
           '4' : ['B','C','F','G'],
           '5' : ['A','C','D','F','G'],
           '6' : ['A','C','D','E','F','G'],
           '7' : ['A','B','C'],
           '8' : ['A','B','C','D','E','F','G'],
           '9' : ['A','B','C','D','F','G']
}
arr = '0123456789'
lst = []
cnt = 0
cand = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if set(my_dict[arr[i]]).difference(set(my_dict[arr[j]])) in lst:
            cnt += 1
            cand.append(set(my_dict[arr[i]]).difference(set(my_dict[arr[j]])))
        if set(my_dict[arr[i]]).difference(set(my_dict[arr[j]])):
            lst.append(set(my_dict[arr[i]]).difference(set(my_dict[arr[j]])))
print(cand)