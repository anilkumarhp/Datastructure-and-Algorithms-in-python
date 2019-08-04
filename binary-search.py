def binary_search(input_list, value):
    try:
        val = input_list.index(value)
        return val
    except ValueError:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

