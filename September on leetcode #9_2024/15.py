

class Solution :
    def isV(ch): 
        return ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch =='a' 
    def findTheLongestSubstring(self, s: str) -> int:
        v = [0]*26 
        mp = dict()
        mp[v] = -1
        ans = 0
        for i in range(len(s)) :
            if self.isV(s[i]) :
                v[s[i]-'a'] = not v[s[i]-'a'] 
            if v not in mp :
                mp[v] = i 
            else :
                ans = max(ans,mp[v])
        return ans 
    
