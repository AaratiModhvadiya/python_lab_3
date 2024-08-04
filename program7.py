def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted into the sorted portion
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Insert the key into its correct position

# Example usage
arr = [1, 4, 2, 8, 23]
insertion_sort(arr)
print(arr)
