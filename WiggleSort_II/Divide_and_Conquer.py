def wiggleSort(nums):
    n = len(nums)
    
    # Helper: Quickselect to find k-th smallest element
    def quickSelect(left, right, k):
        if left == right:
            return nums[left]
        pivot_idx = partition(left, right)
        if k == pivot_idx:
            return nums[k]
        elif k < pivot_idx:
            return quickSelect(left, pivot_idx - 1, k)
        else:
            return quickSelect(pivot_idx + 1, right, k)
    
    # Helper: Partition for quickselect (O(n) per call)
    def partition(left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    # Helper: Virtual index mapping
    def getVirtualIndex(i, n):
        return (1 + 2 * i) % (n | 1)
    
    # Step 1: Find the median in O(n) average time
    median = quickSelect(0, n-1, n//2)
    
    # Step 2: Three-way partition with virtual indexing in O(n)
    left, i, right = 0, 0, n-1
    while i <= right:
        mapped_i = getVirtualIndex(i, n)
        if nums[mapped_i] > median:
            mapped_left = getVirtualIndex(left, n)
            nums[mapped_i], nums[mapped_left] = nums[mapped_left], nums[mapped_i]
            left += 1
            i += 1
        elif nums[mapped_i] < median:
            mapped_right = getVirtualIndex(right, n)
            nums[mapped_i], nums[mapped_right] = nums[mapped_right], nums[mapped_i]
            right -= 1
        else:
            i += 1
    return nums
print(wiggleSort([1,5,1,1,6,4])) # [1,6,1,5,1,4]
print(wiggleSort([1,3,2,2,3,1])) # [2,3,1,3,1,2]