class Solution(object):
    def selfDividingNumbers(self, left, right):
    	result[]
    	for num in range(left,right+1):
    		if self.isSelfDivingNumber(num):
    			result.append(num)
    		return result

    def isSelfDivingNumber(self, num)
    	num_str=str(num)
    	if '0' in num_str:
    		return False
    	else:
    		return all(num%int(i)==0 for i in num_str)
    