import random
import time


def randomized_quicksort(num_list):
    """Sorts an array using Randomized Quicksort."""
    # Base case: empty or single-element array is already sorted
    if len(num_list) <= 1:
        return num_list

    # Choose pivot randomly to reduce input sensitivity
    pivot_index = random.randint(0, len(num_list) - 1)
    pivot = num_list[pivot_index]

    # Partition into three segments to handle duplicates gracefully
    less = []
    equal = []
    greater = []

    for x in num_list:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)

    # Recursive call on left and right partitions
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Use middle element as pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right
    return quick_sort(left) + middle + quick_sort(right)


def main():

    # Randomized quicksort

    start = time.perf_counter()
    list1 = [27, 25, 29, 30, 34, 37, 38, 24, 35, 32, 33, 26, 28, 31]
    print(f"Example1: {list1}")
    print(f"Result: {randomized_quicksort(list1)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    start = time.perf_counter()
    list2 = [12, 89, 5, 5, 9, 9, 0, 12]
    print("Example2:", list2)
    print(f"Result: {randomized_quicksort(list2)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    start = time.perf_counter()
    list3 = [-9, 0, 0, 55, 98, -2, -1]
    print("Example3:", list3)
    print(f"Result: {randomized_quicksort(list3)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    edge_case1 = []
    print(f"Edge Case1: {randomized_quicksort(edge_case1)}")

    edge_case2 = [7]
    print(f"Edge Case2: {randomized_quicksort(edge_case2)}")

    edge_case3 = [9, 9, 9, 9]
    print(f"Edge Case3: {randomized_quicksort(edge_case3)}")

    edge_case4 = [9, 8, 5, 1]
    print(f"Edge Case4: {randomized_quicksort(edge_case4)}\n")

    # Deterministic quicksort

    start = time.perf_counter()
    list1 = [x for x in range(1, 25)]
    print(f"Sorted Array: {list1}")
    print(f"Result: {quick_sort(list1)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    start = time.perf_counter()
    list2 = [99, 98, 97, 96, 94, 93, 93, 91, 90, 89, 88, 87, 86, 85]
    print("Reverse Array:", list2)
    print(f"Result: {quick_sort(list2)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    start = time.perf_counter()
    list3 = [-9, 0, 0, 55, 98, -2, -1]
    print("Random Array:", list3)
    print(f"Result: {quick_sort(list3)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")

    start = time.perf_counter()
    list4 = [5, 5, 6, 767, 9, 9, 0, 34, 56]
    print("Array with repeated elements:", list4)
    print(f"Result: {quick_sort(list4)}")
    print(f"Time taken: {time.perf_counter() - start} seconds\n")


if __name__ == "__main__":
    main()