class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for i in range(len(temperatures))]
        found = [False for i in range(len(temperatures))]
        for i in range(len(temperatures)-1):
            print(temperatures[i])
            for j in range(i, len(temperatures)):
                if found[i] == False:
                    if temperatures[i] >= temperatures[j]:
                        output[i] += 1
                        print(output[i])
                    else:
                        found[i] = True
        print(found)
        for i in range(len(found)):
            print(found[i])
            if not found[i]:
                output[i] = 0

        return output