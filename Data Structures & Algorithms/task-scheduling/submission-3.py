class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = {}
        largest = 0
        for task in tasks:
            tasks_dict[task] = tasks_dict.get(task,0)+1
        largest = max(tasks_dict.values())
        largestcount = 0
        for val in tasks_dict.values():
            if val == largest:
                largestcount += 1
        cycles = max((largest-1)*(n+1)+largestcount, len(tasks))
        return cycles
