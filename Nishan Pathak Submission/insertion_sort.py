def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:  # descending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    # Example usage and testing
    data = [5, 2, 9, 1, 4, 6, 100, -3, 0]
    print("Original list:", data)
    sorted_data = insertion_sort_desc(data)
    print("Sorted list (descending):", sorted_data)
