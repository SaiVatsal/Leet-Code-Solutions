class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        import math
        
        freq = Counter(s)
        half = {}
        mid = ""
        m = 0
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:
                if freq[char] % 2 != 0:
                    mid += char
                half[char] = freq[char] // 2
                m += half[char]
        
        def get_ways(f, target_k):
            ways = 1
            curr_len = 0
            for char in "abcdefghijklmnopqrstuvwxyz":
                count = f.get(char, 0)
                if count > 0:
                    curr_len += count
                    ways *= math.comb(curr_len, count)
                    if ways > target_k:
                        return target_k + 1
            return ways
            
        if get_ways(half, k) < k:
            return ""
            
        first_half = []
        for _ in range(m):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if half.get(char, 0) > 0:
                    half[char] -= 1
                    ways = get_ways(half, k)
                    
                    if ways >= k:
                        first_half.append(char)
                        break
                    else:
                        k -= ways
                        half[char] += 1
                        
        first_str = "".join(first_half)
        return first_str + mid + first_str[::-1]