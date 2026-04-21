class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        visited = [False] * len(strs) 
        for i in range(len(strs)):
            if visited[i]:
                continue 
            similar = [strs[i]]
            visited[i] = True
            d = {}
            for p in strs[i]:
                d[p] = d.get(p, 0) + 1

            for j in range(i + 1, len(strs)):
                if visited[j]:
                    continue
                if len(strs[j]) != len(strs[i]):
                    continue
                t = d.copy()
                is_anagram = True
                for ch in strs[j]:
                    if ch not in t:
                        is_anagram = False
                        break
                    t[ch] -= 1
                    if t[ch] < 0:
                        is_anagram = False
                        break
                if is_anagram:
                    similar.append(strs[j])
                    visited[j] = True
            answer.append(similar)
        return answer




        

        