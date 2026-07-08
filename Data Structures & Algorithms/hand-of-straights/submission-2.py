class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nums = {}
        for i in range(len(hand)):
            if hand[i] in nums:
                nums[hand[i]] += 1
            else:
                nums[hand[i]] = 1
                
        valid = True
        while sum(nums.values()) >= groupSize and valid:
            num = min(k for k, v in nums.items() if v >= 1)
            for i in range(groupSize):
                if num in nums and nums[num] >= 1:
                    nums[num] -= 1
                else:
                    valid = False
                    break
                num += 1
        
        if sum(nums.values()) == 0:
            return True
        return False