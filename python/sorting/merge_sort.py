def merge_sort(some_list: list) -> list:
    print(some_list)
    if len(some_list) > 1:
        mid: int = len(some_list) // 2
        left = some_list[:mid]
        right = some_list[mid:]
        left = merge_sort(left)
        right = merge_sort(right)

        i = 0 # left
        j = 0 # right
        result = []
        
        while i < len(left) and j < len(right):
            if right[j] > left[i]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result
    return some_list
