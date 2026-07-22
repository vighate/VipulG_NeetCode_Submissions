from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        #pattern
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, level = q.popleft()

            if word == endWord:
                return level
            
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                
                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level+1))

        return 0