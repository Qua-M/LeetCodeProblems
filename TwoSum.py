import itertools
class Solution:
    def twoSum(nums, target):
        comb = itertools.combinations(nums, 2)
        for i in comb:
            if i[0] + i[1] == target:
                x = nums.index(i[0])
                nums[nums.index(i[0])] = 'Done'
                y = nums.index(i[1])
                print([x, y])

class Solution2:
    def twoSum(self, nums, target):
        h = {} # Empty Dictionary to add in
        for i, num in enumerate(nums): # enumerate returns alist of tuples (index, value)
            n = target - num # n is the value of the first number and num is the other one
            if n not in h: # if n not in h store a key of num and value of it;s index (we are sure that num is in nums)
                h[num] = i
            else: #if its there return the index of that number and the index of the number iterated
                return [h[n], i]
