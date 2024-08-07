# remove val element from list in-place

def remove_in_place(nums, val):
    updated_index = 0
    for index in range(len(nums)):
        if nums[index] != val:
            nums[updated_index] = nums[index]
            updated_index += 1
    return updated_index
nums = [3, 2, 2, 3, 1, 3, 4]
val = 3
call_function = remove_in_place(nums , val)
print(call_function)
