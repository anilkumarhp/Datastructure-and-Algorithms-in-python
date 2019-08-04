r = int(input("Enter the range"))
arr = []

for i in range(r):
    val = int(input("Enter the Value : "))
    arr.append(val)

skey = int(input("Enter the search element :"))
print(arr)
print(skey)


class BinarySearch:
    def binarysearch(self, a, key):
        lo = 0
        hi = len(a)

        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)
            print("mid %s " % mid)
            if key < a[mid]:
                hi = mid - 1
            elif key > a[mid]:
                lo = mid + 1
            else:
                return mid + 1
        return -1


bs = BinarySearch()
print(bs.binarysearch(arr, skey))
