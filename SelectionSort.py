def Selection_Sort(lst):
    for j in range(len(lst) - 1):
        min_value = j
        for i in range(j, len(lst)):
            if lst[min_value] > lst[i]:
                min_value = i
        lst[j], lst[min_value] = lst[min_value], lst[j]

    return lst


print(Selection_Sort([7, 5, 2, 8, 8]))
