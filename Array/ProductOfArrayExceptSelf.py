def productExceptSelf(nums):
    """
    :param nums: array of numbers
    :return: array of numbers with product except itself
    """
    result = []
    for index,val in enumerate(nums):
        #GO RIGHT
        productNum = 1
        print(index,val)
        for rightindex in range(index+1,len(nums)):
            print('productNum =',productNum,', nums[rightindex] =',nums[rightindex])
            productNum *= nums[rightindex]
        for leftindex in range(index):
            productNum *= nums[leftindex]
        result.append(productNum)
    return result
print(productExceptSelf([1,2,3,4]))
