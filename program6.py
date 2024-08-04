def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        
        # Test against elements after i to find the true minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
elements = [22, 13, 4, 8, 17, 26, 53, 4]
sorted_elements = selection_sort(elements)
print("Sorted array:", sorted_elements)
