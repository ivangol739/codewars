# Given an array of 2k integers (for some integer k), 
# perform the following operations until the array contains only one element:
# On the 1st, 3rd, 5th, etc. 
# iterations (1-based) replace each pair of consecutive elements with their sum;
# On the 2nd, 4th, 6th, etc. 
# iterations replace each pair of consecutive elements with their product.

def array_conversion(arr):
  is_odd = True
  while len(arr) > 1:
    nums = []
    for i in range(0, len(arr), 2):
      if is_odd:
        nums.append(arr[i] + arr[i+1])
      else:
        nums.append(arr[i] * arr[i+1])
    is_odd = not is_odd
    arr = nums
  return arr[0]

print(array_conversion([1, 2, 3, 4, 5, 6, 7, 8]))



