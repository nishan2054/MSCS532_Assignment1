def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  # ascending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    # Example usage and testing
    data = [5, 2, 9, 1, 5, 6]
    print("Original list:", data)
    sorted_data = insertion_sort(data)
    print("Sorted list (ascending):", sorted_data)
