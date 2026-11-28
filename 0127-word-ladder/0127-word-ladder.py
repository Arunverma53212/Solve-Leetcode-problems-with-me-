from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        if endWord  not in wordList: # O(1)
            return 0
        que = deque()  # O (1)
        que.append((beginWord,1))  
        wordList = set(wordList)   # O(1)
        while len(que)!=0:  # O(n)
            word,level = que.popleft() # O(1)
            if word == endWord:  # O(1)
                return level
            for i in range(len(word)):   # O(m)
                for ch in "abcdefghijklmnopqrstuvwxyz":  # O(26)
                    if ch == word[i]: # O(1)
                        continue   
                    new_word = word[:i]+ch+word[i+1:]
                    if new_word in wordList :   # O(1)
                        que.append((new_word,level+1))
                        wordList.remove(new_word)
        return 0


                    




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna