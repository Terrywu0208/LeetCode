class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            rp = r.popleft()
            dp = d.popleft()
            n+=1
            if rp < dp: # "Radiant" ban "Dire"
                r.append(n)
            elif dp < rp: # "Dire" ban "Radiant"
                d.append(n)
        return "Radiant" if r else "Dire"