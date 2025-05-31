def wiggleSort(nums):
    # Step 1: Sort the array
    nums.sort()  # e.g., [1,5,1,1,6,4] -> [1,1,1,4,5,6]
    
    # Step 2: Create a copy of the sorted array
    sorted_nums = nums.copy()  # Avoid modifying while assigning
    
    # Step 3: Find the middle index
    n = len(nums)
    mid = (n - 1) // 2  # e.g., n=6, mid=2
    
    # Step 4: Get smaller and larger halves in reverse order
    smaller_half = sorted_nums[:mid+1][::-1]  # [1,1,1] (indices 0 to 2, reversed)
    larger_half = sorted_nums[mid+1:][::-1]   # [6,5,4] (indices 3 to 5, reversed)
    
    # Step 5: Assign to even indices (valleys)
    even_indices = list(range(0, n, 2))  # [0,2,4]
    for i, val in zip(even_indices, smaller_half):
        nums[i] = val
    
    # Step 6: Assign to odd indices (peaks)
    odd_indices = list(range(1, n, 2))   # [1,3,5]
    for i, val in zip(odd_indices, larger_half):
        nums[i] = val
    return nums
print(wiggleSort([1,5,1,1,6,4])) # [1,6,1,5,1,4]
print(wiggleSort([1,3,2,2,3,1])) # [2,3,1,3,1,2]

# In Place
def wiggleSort_Inplace(nums):
    nums.sort()  
    
    n = len(nums)
    mid = (n - 1) // 2  
    nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
    return nums

print(wiggleSort_Inplace([1,5,1,1,6,4])) # [1,6,1,5,1,4]
print(wiggleSort_Inplace([1,3,2,2,3,1])) # [2,3,1,3,1,2]