# LeetCode Problem: Number of Recent Calls

## Problem Explanation

You are tasked with implementing the `RecentCounter` class, which is designed to count the number of recent requests within a specific time frame. The class has two primary functions:

1. `RecentCounter()`: Initializes the counter with zero recent requests.
2. `ping(int t)`: Adds a new request at time `t`, where `t` represents a time in milliseconds. This function returns the number of requests that have occurred in the past 3000 milliseconds, including the new request. In other words, it returns the count of requests within the inclusive range `[t - 3000, t]`.

It's guaranteed that every call to `ping` will use a `t` value that is strictly larger than the previous call.

### Example:

```python
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output:
[null, 1, 2, 3, 3]
```

**Explanation:**
Suppose you create a `RecentCounter` object using `RecentCounter()`. Then, you execute the following `ping` operations:

1. `ping(1)`: You make the first request at time 1. The range to consider is `[-2999, 1]`, and it returns 1.
2. `ping(100)`: You make a second request at time 100. The range is `[-2900, 100]`, and it returns 2.
3. `ping(3001)`: Your third request is at time 3001. The range is `[1, 3001]`, and it returns 3.
4. `ping(3002)`: You make another request at time 3002. The range is `[2, 3002]`, and it returns 3.

## Solution

```python
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
```

To solve this problem, we can use a queue (deque) to keep track of the timestamps of the requests. We'll follow these steps in the `ping` method:

1. Append the current timestamp `t` to the end of the queue.
2. While the timestamp at the front of the queue is outside the time frame of the last 3000 milliseconds (i.e., less than `t - 3000`), pop the front element from the queue.

This ensures that the queue only contains timestamps within the desired time frame. The length of the queue will represent the count of requests within the last 3000 milliseconds, so we return `len(self.queue)`.

