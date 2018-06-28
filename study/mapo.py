nums = [1,2,3,6,5,4]
for i in range(len(nums)): #负责冒泡次数
    for j in range(i):    #j为下标
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print (nums)