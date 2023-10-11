class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current = 0
        for r in range(len(gain)):
            current += gain[r]
            max_altitude = max(max_altitude, current)
        return max_altitude

