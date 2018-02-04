class Solution(object):
    def arrayPairSum(self, nums):
    	#give an array and sort them from small to large, 1st and 2nd pick the smallest can get the max of all
        nums.sort() #sort an array
        count=0 
        for a in range(0,len(nums)-1,2):#pick 2 numbers from the array from small to large
            count+=nums[a]#add the two number together, cycle
        return count
    