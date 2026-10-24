from math import ceil

class Solution:
    def hoursToEat(self, piles: List[int], speed: int) -> int:
        h = 0
        for pile in piles:
            h += ceil(pile / speed)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        min_speed_hours_to_eat = self.hoursToEat(piles, min_speed)
        max_speed = max(piles)
        max_speed_hours_to_eat = self.hoursToEat(piles, max_speed)
        while min_speed <= max_speed:
            if min_speed_hours_to_eat == h or min_speed_hours_to_eat == max_speed_hours_to_eat:
                return min_speed
            
            if max_speed - min_speed == 1:
                if min_speed_hours_to_eat < h:
                    return min_speed
                else:
                    return max_speed

            mid_speed = min_speed + (max_speed - min_speed + 1) // 2
            mid_speed_hours_to_eat = self.hoursToEat(piles, mid_speed)
            if mid_speed_hours_to_eat <= h:
                max_speed = mid_speed
                max_speed_hours_to_eat = mid_speed_hours_to_eat
            else:
                min_speed = mid_speed + 1
                min_speed_hours_to_eat = self.hoursToEat(piles, min_speed)
        raise ValueError("Why me?")
