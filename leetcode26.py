def removeDuplicates(nums: list):
    previous = nums[0]
    i=1
    count=1
    while count < len(nums):
        count+=1
        print(nums[i])
        if nums[i]==previous:
            nums.append(nums[i])
            del nums[i]
        else:
            previous=nums[i]
            i+=1
    return i