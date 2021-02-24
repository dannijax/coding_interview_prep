def search_range(num, target):
    if not num:
        return [-1, -1]
    else:

        left_index = -1
        right_index= -1
        for i in range(len(num)):
            if num[i] == target:
                left_index = i
                break
        for j in range(len(num) -1, -1, -1):
            if num[j] == target:
                right_index = j
                break
        return [left_index, right_index]


#print(search_range([5,7,7,8,8,10], 8))
#print(search_range([5,7,7,8,8,10], 5))
#print(search_range([], 6))

# def find_extreme_index(nums, target, direction):
#     lo = 0
#     high = len(nums)
#     while lo < high :
#         mid = (lo + high) //2
#         if nums[mid] > target or direction and nums[mid] == target :
#             high = mid
#         else:
#             lo = mid + 1
# 	return lo

# def search_range(nums, target):
# 	left_index= find_extreme_index(nums, target, True)
# 	if nums[left_index] != target or left_index ==len(nums):
# 		return [-1, -1]
# 	return [left_index, find_extreme_index(nums, target, False)]


# Given an array of size N, prefilled with values. Left shift all non zero values and merge adjacent same value cells.

# Examples:
# 	[1, 0, 2] -> [1, 2, 0]
# 	[0, 0, 2, 1] -> [2, 1, 0, 0]
# 	[1, 0, 1] -> [2, 0, 0]
# 	[0, 2, 2, 1] -> [4, 1, 0, 0]
# 	[1, 1, 1] -> [2, 1, 0]
# 	[1, 1, 1, 1] -> [2, 2, 0, 0]
#     ####[1, 0, 2] -> [1, 2, 0]
# 	[0, 0, 2, 1] -> [2, 1, 0, 0]
# 	[1, 0, 1] -> [2, 0, 0]
# 	[0, 2, 2, 1] -> [4, 1, 0, 0]
# 	[1, 1, 1] -> [2, 1, 0]
# 	[1, 1, 1, 1] -> [2, 2, 0, 0]
  
  ##
  #Scan through the array
  #Check for non- zero numbers
  #if number is greater that zero
  
  
def merge_elements(a, b):
    return a + b
  

# def left_shift(arr):  
#   if len(arr <= 1):
#     return arr
  
#   prev_index = 0
#   for i in range(len(arr)):
#     if arr[i] > 0:
#       if prev_index > 0:
#         if arr[prev_index] == arr[i]:
#           res = merge_elements(arr[prev_index, arr[i]])
#           arr[prev_index] = res
#           prev_index = i
#         else:
#           prev_index = i + 1
          
#       else:
#          if arr[i + 1] == arr[1]:
#             res = merge_elements(arr[i + 1], arr[i])
#             arr[prev_index] = res
#             prev_index +=1

def left_shift(arr):
    count = 0

    while count < len(arr)
        if (arr[i] != 0):
            arr[count] = arr[i]
            count +=1
        if arr[i] == arr[i + 1]:
            res = arr[i] + arr[i +1]
            arr[i] = res
            arr[i+1] = 0



    # while (count < len(arr)) :
    #     count +=1
    #     arr[count] = 0

    # while count < len(arr): 
    #     arr[count] = 0
    #     count += 1

    print(arr)

left_shift([0, 0, 2, 1])
