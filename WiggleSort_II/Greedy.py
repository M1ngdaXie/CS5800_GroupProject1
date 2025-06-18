def wiggleSort(nums):
    temp = nums.copy()
    temp.sort(reverse=True)
    for i in range(1,len(nums),2):
        nums[i] = temp.pop(0)
    for i in range(0,len(nums),2):
        nums[i] = temp.pop(0)
    return nums
print(wiggleSort([1,5,1,1,6,4])) # [1,6,1,5,1,4]
print(wiggleSort([1,3,2,2,3,1])) # [2,3,1,3,1,2]
