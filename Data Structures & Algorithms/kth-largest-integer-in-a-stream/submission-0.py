class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.integers = nums
        self.largest = k    

    def add(self, val: int) -> int:
        self.integers.append(val)
        self.integers.sort()
        return self.integers[len(self.integers)-self.largest]

        
