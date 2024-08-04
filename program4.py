def sequential_search(elements, target):
    for index, value in enumerate(elements):
        if value == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# List of elements
elements = [1, 3, 5, 8, 10, 23, 35]

# Target value to search for
target = 10

# Perform the search
index = sequential_search(elements, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
