def linear_search(ls, k):
    """
        Algorithm Linear Search:

        input:
            1) a list of integer values
            2) key value to be searched

        output:
            if found, prints the position of the integer.
            if not found, prints element not found.
    """
    # Algorithm Logic
    try:
        pos = ls.index(k)  # using inbuilt list method index()
        print(f'List : {ls}')
        print(f'{k} is found at position {pos + 1}.')
    except ValueError as ve:
        print(f'List : {ls}')
        print(ve)


a = []
key = 0
while True:
    try:
        print("Enter the length of the list")
        n = int(input())
        while n:
            try:
                print("Enter the value")
                val = int(input())
                a.append(val)
                n -= 1
            except ValueError:
                print("Enter valid integer\n")

        while True:
            print("Enter the value to be searched:")
            try:
                key = int(input())
                break
            except ValueError:
                print("Enter valid integer \n")
        break
    except ValueError:
        print("Enter valid integer \n")

linear_search(a, key)

# a = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
# linear_search(a, 13)
