def hammingWeight(n):
    list_ = list(str(n))
    int_list = [int(i) for i in list_]
    return sum(int_list)

print(hammingWeight(1011))