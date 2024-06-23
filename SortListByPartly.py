def sort_array_by_parity(nums):
  # Initialize pointers
  even_pointer = 0
  odd_pointer = len(nums) - 1

  # Use while loop to move even and odd pointers towards the center
  while even_pointer < odd_pointer:
    # Move even_pointer until it points to an odd number
    while even_pointer < len(nums) and nums[even_pointer] % 2 == 0:
      even_pointer += 1

    # Move odd_pointer until it points to an even number
    while odd_pointer >= 0 and nums[odd_pointer] % 2 != 0:
      odd_pointer -= 1

    # Swap elements if even_pointer is less than odd_pointer
    if even_pointer < odd_pointer:
      nums[even_pointer], nums[odd_pointer] = nums[odd_pointer], nums[
          even_pointer]
      even_pointer += 1
      odd_pointer -= 1

  return nums


nums = [3, 1, 2, 4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))