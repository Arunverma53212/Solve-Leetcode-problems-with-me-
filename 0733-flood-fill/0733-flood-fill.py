from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        que = deque()
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        que.append((sr, sc))
        image[sr][sc] = color

        while que:
            i, j = que.popleft()

            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i, new_j = i+x, j+y

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if image[new_i][new_j] != original:
                    continue

                image[new_i][new_j] = color
                que.append((new_i, new_j))

        return image

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna