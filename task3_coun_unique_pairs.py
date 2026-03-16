def count_pairs(nums_list, target):
    s = set()

    for i in range(len(nums_list)):
        for j in range(i + 1, len(nums_list)):
            if nums_list[i] + nums_list[j] == target:
                pair = tuple(sorted([nums_list[i], nums_list[j]]))
                s.add(pair)

    print(s)
    return len(s)

print(count_pairs([1, 3, 2, 2, 3], 5))