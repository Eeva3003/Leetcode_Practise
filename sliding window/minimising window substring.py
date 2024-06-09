#neetcode approach but time limit exceeded 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        countT,window={},{}

        for c in t:
            countT[c]=1+countT.get(c,0)

        have,need=0,len(countT)
        res,reslen=[-1,-1],float("infinity")    
        l=0
        
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                #update result
                if(r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                    #pop from window left
                    window[s[l]]-=1
                    if s[l] in countT and window[s[l]]<countT[s[l]]:
                        have-=1
                    l+=1
        l,r=res
        return s[1:r+1] if reslen in float("infinity") else ""                

        #solution 2
      class Solution(object):
    def minWindow(self, s, t):
        mp1 = defaultdict(int)
        count = len(t)
        for i in t:
            mp1[i] += 1

        i, j, mini, start = 0, 0, len(s) + 1, 0
        while j < len(s):
            if s[j] in mp1 and mp1[s[j]] > 0:
                count -= 1
            if s[j] in mp1:
                mp1[s[j]] -= 1

            while count == 0:
                if mini > j - i + 1:
                    mini = j - i + 1
                    start = i
                if s[i] in mp1:
                    mp1[s[i]] += 1
                    if mp1[s[i]] > 0:
                        count += 1
                i += 1
            j += 1

        if mini == len(s) + 1:
            return ""
        return s[start:start + mini]
