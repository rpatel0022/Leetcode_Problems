#Return False is if unique
#Re

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