#reverse a string
class Solution(object):
    def reverseString(self, s):
        return s[::-1]
        #####x[::-1]
        
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)
    #################################################################################reverse the word within the string
    class Solution(object):
    def reverseWords(self, s):
        return " ".join(map(lambda x: x[::-1], s.split()))
        									#s.split()means to treat each word as a whole instead of treated each alphabete individually
        					#lambda x:x[::-1] =like a calculation function to apply all the element after the , x[::-1] means to reverse the thing after ,
        				# map means apply the function to the thing after,
        		#" ".join means make all isolate words into one sentence
