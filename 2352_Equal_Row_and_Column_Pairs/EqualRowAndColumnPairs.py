class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cal_map = {}
        count = 0
        for i in grid:
            cal_map[tuple(i)] = cal_map.get(tuple(i),0) + 1
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            count += cal_map.get(tuple(tmp),0)
        return count