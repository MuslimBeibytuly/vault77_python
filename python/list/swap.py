def swap(l: list) -> None:
    temp = l[0]
    l[0] = l[len(l) - 1]
    l[len(l) - 1] = temp

l = [1, 2, 3]
print(l)
swap(l=l)
print(l)

# int n = 5
# int shared_ptr<int> n = new shared_ptr<int>(new int(5));
# int * n = new int(5);
# int * n = malloc(sizeof(int));
# int & n = 5;
