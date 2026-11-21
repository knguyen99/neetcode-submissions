class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = reversed(sorted(zip(position, speed)))

        fleet = []

        for pos, speed in cars:
            eta = (target - pos) / speed
            if not fleet or fleet[-1] < eta:
                fleet.append(eta)
        
        return len(fleet)