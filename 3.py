class Solution(object):
    def judgeCircle(self, moves):
        x,y=0,0
        dic={"U":[0,1],"D":[0,-1],"R":[1,0],"L":[-1,0]}
        for m in moves:
        	x,y = x+dic[m][0], y+dic[m][1]
        return (x==0) and (y==0)