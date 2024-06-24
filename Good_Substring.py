#Understand
#We are checking a substring of length 3.
#If that substring is unique than count that as a good substring
#What if there is a string that is less than length 3?


#Plan
#We can create a window for the substring
#To check if it is unique we can use the set.
#Then add the counter if it is unique
#Implementation
def count_good_substrings(s):
  Counter = 0
  for i in range(len(s) - 2):
    window = s[i:i + 3]
    if len(window) == len(set(window)):
      Counter += 1
  return Counter


s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))