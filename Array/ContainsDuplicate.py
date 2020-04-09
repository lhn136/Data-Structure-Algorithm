from collections import defaultdict
def containsDuplicate(nums):
    dupdict = defaultdict(int)
    for i in nums:
        dupdict[i]+=1

    for i in dupdict:
        if dupdict[i]>1:
            return True
    return False
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
