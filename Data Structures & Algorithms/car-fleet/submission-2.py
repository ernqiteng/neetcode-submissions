class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)] 
        #create an array of pairs by iterating through 2 arrays at the same time using zip
        #or could use a hash map and sort through the list

        stack = []
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s) #time taken to reach end
            #does it overlap?
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                #checks if the car reaches the destination before the one ahead of it
                #collision
                stack.pop()
        return(len(stack))