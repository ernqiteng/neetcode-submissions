class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_dict = {}
        largest = 0
        for i in range(len(tasks)):
            if tasks[i] in tasks_dict.keys():
                tasks_dict[tasks[i]] += 1
            else:
                tasks_dict[tasks[i]] = 1
        largest = max(tasks_dict.values())
        largestcount = 0
        for val in tasks_dict.values():
            if val == largest:
                largestcount += 1
        cycles = max((largest-1)*(n+1)+largestcount, len(tasks))
        return cycles
