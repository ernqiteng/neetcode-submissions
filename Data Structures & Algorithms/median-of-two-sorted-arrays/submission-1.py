class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []
        p1 = 0
        p2 = 0
        while (len(nums1)) != p1 and (len(nums2)) != p2:
            if nums1[p1] <= nums2[p2]:
                combined.append(nums1[p1])
                p1 += 1
            else:
                combined.append(nums2[p2])
                p2 += 1

        if len(nums1) == p1:
            for i in range(p2, len(nums2)):
                combined.append(nums2[i])
        if len(nums2) == p2:
            for i in range(p1, len(nums1)):
                combined.append(nums1[i])
        print(combined)
        if len(combined)%2 == 1:
            return combined[(len(combined)//2)]
        else:
            lowermid = combined[((len(combined))//2)-1]
            uppermid = combined[(len(combined))//2]
            print(lowermid, uppermid)
            return (lowermid + uppermid)/2