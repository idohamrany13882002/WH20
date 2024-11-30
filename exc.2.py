def remove_duplicates(l1: list[int]):
    result: list[int] = []

    for i in range(0, len(l1)):
        if l1[i] != l1[i - 1]:
            result.append(l1[i])

    print(result)


remove_duplicates([1, 1, 2, 3, 4, 4, 4])  # to check
