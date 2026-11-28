from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        if endWord  not in wordList:
            return 0
        que = deque()
        que.append((beginWord,1))
        wordList = set(wordList)
        while len(que)!=0:
            word,level = que.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    new_word = word[:i]+ch+word[i+1:]
                    if new_word in wordList :
                        que.append((new_word,level+1))
                        wordList.remove(new_word)
        return 0


                    




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna