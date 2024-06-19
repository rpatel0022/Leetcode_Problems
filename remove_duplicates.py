class Solution:

    #We are given a ordered list of integers. We have to remove duplicates 
    # and return how many duplicates were present

    #We will be comparing the nums[i] with the previous value to see if it is unique. 
    #If it is unique then it would replace nums[i] with nums[j] and increment j
        
    #If it is not than i will continue to increment and j will remain the same there until found another unique pair. 
    def removeDuplicates(self, nums):
        dup_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[dup_count] = nums[i]
                dup_count += 1
        return dup_count