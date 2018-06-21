#TwoSum - Easy - 6.21
def sumlist(nums, target):
    yes = []
    for i in range(len(nums)):
        for j in range(len(nums)+1):
            if (nums[i] + nums[j] == target):
                yes.append(i)
                yes.append(j)
                return yes
            else: 
                pass
       

List = [2, 7, 11, 15]
target = 9
print(sumlist(List, target))
