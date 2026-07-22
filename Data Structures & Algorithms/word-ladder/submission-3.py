from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        q = deque({(beginWord,1)})

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)

        visited = set()
        visited.add(beginWord)
        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]

                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,steps+1))
        return 0




