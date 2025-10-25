"""
Insertion Sort Algorithm (Monotonically Decreasing Order)

This program implements the insertion sort algorithm that sorts
a list of numbers in *descending* order.

Algorithm Explanation:
----------------------
Insertion Sort works by building the sorted portion of the list
one element at a time. At each iteration, the algorithm removes
one element from the unsorted portion and inserts it into its
correct position in the sorted portion.

To achieve descending order, the comparison is reversed:
we move elements that are *smaller* than the current key
one position to the right.

Complexity:
-----------
Time Complexity:
    - Best Case (Already sorted descending): O(n)
    - Average and Worst Case: O(n^2)
Space Complexity:
    - O(1) (In-place sorting)
"""
def insertion_sort_desc(arr):
    """
    Sorts the input list 'arr' in descending order using insertion sort.

    Parameters:
        arr (list): List of comparable elements (e.g., integers or floats)

    Returns:
        list: The same list object, sorted in descending order
    """
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
