import random
import time

def linear_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l , target, low, high):
    if high < low:
        return -1
    mid = (low + high) //2 
    if l[mid] == target:
        return mid
    elif target < l[mid]:
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l , target, mid+1, high)

if __name__ == '__main__':
    x = input("Enter a list of numbers in ascending order separated by spaces: ")
    l1 = list(map(int,x.split()))

    target = int(input("Enter the number to search for: "))

    print("User's list:", l1)
    print("Target:", target)

    start = time.perf_counter()
    linear_result = linear_search(l1, target)
    end = time.perf_counter()
    linear_time = end - start

    start = time.perf_counter()
    binary_result = binary_search(l1, target,0,len(l1)-1)
    end = time.perf_counter()
    binary_time = end - start
    if linear_result != -1:
        print("Naive search found the target at index:", linear_result)
    else:
        print("Naive search did not find the target.")

    if binary_result != -1:
        print("Binary search found the target at index:", binary_result)
    else:
        print("Binary search did not find the target.")

    print("Naive search time:", linear_time, "seconds.")
    print("Binary search time:", binary_time, "seconds.")
