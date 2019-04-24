def has(n, arr):
    for i in arr:
        if n == i:
            return True
    return False

def first(l):
    return l[0]

def has_binary(n, arr):
    begin = 0
    end = len(arr) - 1
    while end - begin > 2:
        mid = int(
            (end + begin) / 2
        )
        if arr[mid] == n:
            return True
        if arr[mid] > n:
            end = mid - 1
        if arr[mid] < n:
            begin = mid + 1
    return arr[begin] == n or arr[end] == n

numbers = [1, 2, 3, 4, 5]
evens = [2, 4, 6, 8, 10]
n = 4
m = 6

# print(has(n, numbers))
# print(has(m, numbers))

# best case: 1, n = arr[0]
# average/worst case: len(arr), n = arr[-1] or n not in arr
# T(n) = O(n), n - len(arr) example of: y = f(x) = kx
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmqWvDZw8zImNQyxD8Ah3Ig7q-B-z3-BHwxXiH4OQCeqdU26cI

# print(first(numbers))
# best/average/worst case: 1
# T(n) = O(1), y = f(x) = 4
# https://www.varsitytutors.com/assets/vt-hotmath-legacy/hotmath_help/topics/constant-function/constant-function-image002.gif

# print(has_binary(6, evens))
# T(n) = O(logn)
# log2(4) = 2, log2(256) = 8

# T(n) = O(nlogn) - quicksort + mergesort
# T(n) = O(n ^ 2) - bubble sort
# T(n) = O(n ^ 3) - ML
# T(n) = O(e ^ n) - exp = 2.7...
# T(n) = O(n!) - Traveler's path

# 1, 2, 
# 3
# 4, 
# 5
# [] 
# 6
# 7, 8, 9, 10
#                     6
#         3                           8
#     2       4                   7       9
# 1               5            7.5              10
# log2(16)