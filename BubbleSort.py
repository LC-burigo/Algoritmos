def Bubble_Sort(lst):
    size = len(lst)
    for ind in range(size - 1):
        for i in range(size - ind - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


arr = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]
print(Bubble_Sort(arr))
