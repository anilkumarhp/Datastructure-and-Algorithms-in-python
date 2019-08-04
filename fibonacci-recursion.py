import time

st = time.time()
# n = int(input("Enter the range \n")) - 2
# fib = [0, 1]
# j = 0
# k = 1
#
# while n:
#     fib.append(fib[j] + fib[k])
#     k = k + 1
#     j = j + 1
#     n = n - 1

fib =[]
n = int(input("Enter the range( a positive integer )\n"))
[fib.append(fib[-1] + fib[-2]) if x > 1 else fib.append(x) for x in range(n)]

print(fib)

print("\n\n----%.2f----" % (time.time() - st))



