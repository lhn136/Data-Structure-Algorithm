from collections import defaultdict
def singleNumber(nums):
    '''
    return the single value number in array

    :param nums: array of nums
    :return: int
    '''
    ArrayDup = defaultdict(int)

    for num in nums:
        ArrayDup[num] += 1


    for num,count in ArrayDup.items():
        if count == 1:
            return num


print(singleNumber([1,2,1]))

print(singleNumber([1,2,3,2,1]))

print(singleNumber([4,1,2,1,2]))
