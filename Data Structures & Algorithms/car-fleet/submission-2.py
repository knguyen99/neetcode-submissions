class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        fleet = []

        for pos, speed in cars:
            eta = (target - pos) / speed
            while fleet and fleet[-1] <= eta:
                fleet.pop()
            fleet.append(eta)
        
        return len(fleet)