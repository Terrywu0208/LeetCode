# LeetCode Problem: Dota2 Senate

## Problem Explanation

In the world of Dota2, there are two parties: the Radiant and the Dire. The Dota2 Senate consists of senators from these two parties who want to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of two rights:

- Ban one senator's right: A senator can make another senator lose all their rights in this and all the following rounds.
- Announce the victory: If a senator finds that the remaining senators with voting rights all belong to the same party, they can announce the victory and decide on the game change.

You are given a string `senate` representing each senator's party affiliation. The characters 'R' and 'D' represent the Radiant and the Dire parties. If there are n senators, the size of the given string will be n. The round-based procedure starts from the first senator to the last senator in the given order and continues until the end of voting. All senators who have lost their rights will be skipped during the procedure.

Your task is to predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

### Example:

#### Example 1:

Input:
```
senate = "RD"
```

Output:
```
"Radiant"
```

Explanation: 
- The first senator comes from Radiant and bans the next senator's right in round 1. 
- The second senator can't exercise any rights anymore since their right has been banned. 
- In round 2, the first senator can announce the victory since they are the only one left with voting rights in the Senate.

#### Example 2:

Input:
```
senate = "RDD"
```

Output:
```
"Dire"
```

Explanation: 
- The first senator comes from Radiant and bans the next senator's right in round 1. 
- The second senator can't exercise any rights anymore since their right has been banned. 
- The third senator comes from Dire and bans the first senator's right in round 1. 
- In round 2, the third senator can announce the victory since they are the only one left with voting rights in the Senate.

## Solution

```python
from collections import deque

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
            n += 1
            if rp < dp: # "Radiant" bans "Dire"
                r.append(n)
            elif dp < rp: # "Dire" bans "Radiant"
                d.append(n)
        return "Radiant" if r else "Dire"
```

This code simulates a game where two groups, "Radiant" (R) and "Dire" (D), try to eliminate each other. It uses two deques, `r` and `d`, to keep track of the players in each group. The game proceeds as follows:

1. The code scans the `senate` string and places each player in their respective group deque.

2. In a loop, it simulates a banning process:
   - It removes one player from each group (the earliest in the game).
   - It increments `n` to indicate a round of banning.
   - If the "Radiant" player bans the "Dire" player (index comparison), the "Dire" player is pushed back with an incremented index; vice versa for "Dire" banning "Radiant."

3. The loop continues until one group's deque is empty, indicating that the other group has won.

4. The winner is determined by checking which group's deque is non-empty, and their name is returned.

