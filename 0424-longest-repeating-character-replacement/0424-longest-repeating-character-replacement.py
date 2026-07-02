class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        res=0
        dic={}
        while l<=r and r<len(s):
            windowlen=r-l+1
            if s[r] not in dic:
                dic[s[r]]=1
            else:
                dic[s[r]]+=1
                
            highestfreq=max(dic.values())

            if windowlen-highestfreq<=k:
                res=max(res,windowlen)
                r+=1
            else:         
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l+=1
                r+=1
            
        return res