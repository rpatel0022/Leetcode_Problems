#Understand
#Trying to find the largest positive and negative pair.
#Only contains positive and negative numbers
#What would happen is the list is empty?

#Plan
#We can use a dictionary to keep track of the largest_k and then compare if the negative of that is already in the dictionary if it is then see if it is larger.


#Implementation
def find_largest_k(nums):
  num_dict = {}
  largest_k = -1

  for num in nums:
    num_dict[num] = True

    if -num in num_dict:
      largest_k = max(largest_k, abs(num))

  return largest_k


# Example usage
nums = [-1, 2, -3, 3, -1]
print(find_largest_k(nums))  # Output: 3

nums2 = [-10, 2, 7, -3]
print(find_largest_k(nums2))  # Output: -1