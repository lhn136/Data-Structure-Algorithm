from collections import defaultdict

def twoSum(nums,target):
    """

    :param nums: array of numbers
    :param target: target sum of two numbers
    :return: an array with two interger
    """
    indexSumDict = defaultdict(int)
    for index in range(0,len(nums)):
        indexSumDict[target-nums[index]]=index
    print(indexSumDict)
    for index in range(0,len(nums)):
        if nums[index] in indexSumDict:
            if index != indexSumDict[nums[index]]:
                print(index,indexSumDict[nums[index]])
                #return [index,indexSumDict[nums[index]]]
    return []

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))

print(twoSum([-1,-2,-3,-4,-5],-8))