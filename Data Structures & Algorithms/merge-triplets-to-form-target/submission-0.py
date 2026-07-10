class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validtriplets = []
        for triplet in triplets:
            valid = True
            for index in range(3):
                if triplet[index] > target[index]:
                    valid = False
                    break
            if valid:
                validtriplets.append(triplet)
        
        found = 0
        for index in range(3):
            if any(triplet[index] == target[index] for triplet in validtriplets):
                found += 1
        
        if found == 3:
            return True
        return False

        