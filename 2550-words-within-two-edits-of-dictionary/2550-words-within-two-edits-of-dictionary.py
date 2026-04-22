class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def _get_distance(s1,s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    cnt+=1
                if cnt==3:
                    return False
            return True
        good = []
        for query in queries:
            for d in dictionary:
                dist = _get_distance(query,d)
                if dist:
                    good.append(query)
                    break
        return good