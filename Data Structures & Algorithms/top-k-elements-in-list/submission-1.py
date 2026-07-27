class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct={}
        fq=[[]for i in range(len(nums)+1)]
        for n in nums:
            ct[n]=1+ct.get(n,0)
        for n,c in ct.items():
            fq[c].append(n)
        r=[]
        for i in range(len(fq)-1,0,-1):
            for n in fq[i]:
                r.append(n)
                if len(r)==k:
                    return r