from collections import deque

class Solution:
    def isCycle(self, adj: list) -> bool:

        visited = [0] * len(adj)

        for i in range(len(adj)):

            if visited[i] == 0:

                deq = deque()
                deq.append((i, -1))
                visited[i] = 1

                while deq:

                    node, parent = deq.popleft()

                    for n in adj[node]:

                        if visited[n] == 0:
                            visited[n] = 1
                            deq.append((n, node))

                        elif n != parent:
                            return True

        return False



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna