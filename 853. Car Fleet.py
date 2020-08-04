class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort()
        leaders, slowest = 0, 0
        for p,s in cars[::-1]:
            time = (target-p)/s
            if time > slowest:
                leaders += 1
                slowest = time
        return leaders
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def thoughtTooMuchCarFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # traverse array in reverse from l-1 to 0
        # check if they catch-up to one ahead, if yes, update speed.
        # also update their position - 
        # to the one at which they have caught with front car.
        # Keep an array of fleet leaders for each car. If a car doesnt catchup
        # If 'a' catches up to 'b', it will inherit leader from 'b', 
        # else 'a' is its own leader
        # (when we update speed, it will always decrease.)
        # So if car 'a' would have caught up with 'b', 
        # it will still catch up with 'b' even after updating 'b's speed
        
        l = len(position)
        leaders = [l-1]*l
        return 0