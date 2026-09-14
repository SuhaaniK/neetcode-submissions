class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        leader_time = 0 
        for p,s in cars:
            time_to_target = (target - p)/s
            if time_to_target > leader_time:
                fleets+=1 
                leader_time = time_to_target
        return fleets