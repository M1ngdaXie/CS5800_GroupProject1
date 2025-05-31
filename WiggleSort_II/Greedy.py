def wiggleSort(nums):
    # Step 1: Sort a copy of the array
    sorted_nums = sorted(nums)  # e.g., [1,5,1,1,6,4] -> [1,1,1,4,5,6]
    n = len(nums)
    
    # Step 2: Initialize pointers for smallest and largest numbers
    small = 0  # Points to smallest number
    large = n - 1  # Points to largest number
    
    # Step 3: Create result array to avoid in-place issues
    result = [0] * n
    
    # Step 4: Assign numbers greedily to valleys (even) and peaks (odd)
    for i in range(n):
        if i % 2 == 0:  # Even index (valley): assign smallest number
            result[i] = sorted_nums[small]
            small += 1
        else:  # Odd index (peak): assign largest number
            result[i] = sorted_nums[large]
            large -= 1
    
    return result
print(wiggleSort([1,5,1,1,6,4])) # [1,6,1,5,1,4]
print(wiggleSort([1,3,2,2,3,1])) # [2,3,1,3,1,2]