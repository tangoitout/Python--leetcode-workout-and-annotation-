#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#from discussion
def numJewelsInStones(self, J, S):         
	stones = Counter(S)         

return sum([stones[s] for s in stones.keys() if s in set(J)])

class Solution(object):
    def numJewelsInStones(self, J, S):
        count=0
        for x in J:
            if x in S:
                count+=1
                elif count=0
        return count
