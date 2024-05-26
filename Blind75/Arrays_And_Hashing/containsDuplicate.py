# Duplicate Integer

# Given an integer array, nums, return true if any value appears
# more than once in the input array, otherwise return false. 

def hasDuplicate(nums: list[int]):
    # using python set 
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False

nums = [1,2,3,4,4]

test = hasDuplicate(nums)
print(test)