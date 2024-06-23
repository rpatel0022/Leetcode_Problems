#Return False is if unique
#Return True if it contains duplicate values

#Use dictionary to keep track of the occurrences. 
#If occurences is very more than or equal to two then it contains duplicates and return True. 

class Solution(object):
    def containsDuplicate(self, nums):
        dic = {} 

        for i in nums: 
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in nums:
            if dic[i] >= 2:
                return True
        
        return False