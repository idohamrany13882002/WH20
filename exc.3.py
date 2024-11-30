def merge_lists(l1: list[int], l2: list[int]):
    l3: list[int] = []
    for i in range(len(l1)):
        if l1[i] >= l2[i]:
            l3.append(l2[i])
            l3.append(l1[i])
        else:
            l3.append(l1[i])
            l3.append(l2[i])

    print(l3)


merge_lists([1, 2, 4], [1, 3, 4])  # to check
