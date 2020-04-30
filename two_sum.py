#https://leetcode.com/problems/two-sum/

nums = [3, 3, 11, 15]
#print(nums.index(11))
#print(nums[nums.index(15)+1:])
target = 6
for i in range(len(nums)):
    #print(i)
    temp = target - nums[i]
    for j in range(i+1, len(nums)):
        #print(i, j)
        if temp == nums[j]:
            print([i, j])

    # temp = target - i
    # for i in range(len(nums)):
    #     if temp == j:
    #         print([nums.index(i), nums.index(j)])
