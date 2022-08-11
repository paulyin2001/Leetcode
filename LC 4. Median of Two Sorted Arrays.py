class Solution:
    def findMedianSortedArrays(self, nums1: "list[int]", nums2: "list[int]") -> float:
        total = len(nums1) + len(nums2)
        half = total // 2 #if 4, 2. (nums1[2] + nums2[3])/2. if 5, 2. nums[2]
        numsS, numsL = nums1, nums2   #short nums, long nums
        if len(numsS) > len(numsL):
            numsS, numsL = numsL, numsS
        
        leftS, rightS = 0, len(numsS) - 1
        while True:     #must have mediam
            #partition numsS
            #midS = leftS + (rightS - leftS + 1) // 2
            midS = leftS + (rightS - leftS) // 2
            S_rightMost = numsS[midS] if midS >= 0 else float('-inf')
            S_leftMostS = numsS[midS+1] if midS+1 < len(numsS) else float('inf')
            
            #partition numsL
            midL = half - (midS+2)
            L_rightMost = numsL[midL] if midL >= 0 else float('-inf')
            L_leftMost = numsL[midL+1] if midL+1 < len(numsL) else float('inf')
            
            rightMost = max(S_rightMost, L_rightMost)
            leftMost = min(S_leftMostS, L_leftMost)
            
            if rightMost <= leftMost:
                return (rightMost + leftMost) / 2 if total % 2 == 0 else leftMost
            
            #invalid partition. overlap. shorten numsS left partition or not?
            if S_rightMost < L_rightMost: #L overlap. extend S
                leftS = midS + 1
            else:                       #S overlap. shorten S
                rightS = midS - 1
        
testcase1 = [[1,3], [2]]
s = Solution()
print(s.findMedianSortedArrays(testcase1[0], testcase1[1]))
testcase1 = [[1,3], [2,4]]
print(s.findMedianSortedArrays(testcase1[0], testcase1[1]))