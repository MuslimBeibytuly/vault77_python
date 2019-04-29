def is_wrong(num: int) -> bool:
    return len({
        int(num / 100),
        int((int(num % 100)) / 10), 
        int(num % 10)
    }) < 3

    
def gaussian_sum(l):
    return sum(x for x in l if not is_wrong(x))

print(gaussian_sum([222, 333, 232, 456, 123, 323]))
