class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        type_arr = []
        start = []
        end_idx = []
        i = 0
        while i < n:

            j = i
            while j < n and s[j] == s[i]:
                j += 1
            type_arr.append(int(s[i]))
            start.append(i)
            end_idx.append(j - 1)
            i = j
        N = len(type_arr)
        pos_to_seg = [0] * n
        for idx in range(N):
            for j in range(start[idx], end_idx[idx] + 1):
                pos_to_seg[j] = idx
                
        ans = [0] * N
        for idx in range(1, N - 1):
            if type_arr[idx] == 1:
                ans[idx] = (end_idx[idx - 1] - start[idx - 1] + 1) + (end_idx[idx + 1] - start[idx + 1] + 1)
                
        log_table = [0] * (N + 1)
        for idx in range(2, N + 1):

            log_table[idx] = log_table[idx // 2] + 1
            
        K = log_table[N] + 1
        st = [[0] * N for _ in range(K)]
        
        for idx in range(N):
            st[0][idx] = ans[idx]
            
        for j in range(1, K):
            for idx in range(N - (1 << j) + 1):
                st[j][idx] = max(st[j - 1][idx], st[j - 1][idx + (1 << (j - 1))])
                
        def query_rmq(L_q, R_q):
            if L_q > R_q:
                return 0
            j = log_table[R_q - L_q + 1]
            return max(st[j][L_q], st[j][R_q - (1 << j) + 1])
            
        def eval_seg(idx, L, R, segL, segR):
            if idx <= segL or idx >= segR: return 0
            if type_arr[idx] == 0: return 0
            
            if idx - 1 == segL:
                left_len = max(0, end_idx[idx - 1] - L + 1)
            else:
                left_len = end_idx[idx - 1] - start[idx - 1] + 1
                
            if idx + 1 == segR:
                right_len = max(0, R - start[idx + 1] + 1)
            else:
                right_len = end_idx[idx + 1] - start[idx + 1] + 1
                
            return left_len + right_len

        res = []

        for L, R in queries:
            segL = pos_to_seg[L]
            segR = pos_to_seg[R]
            
            if segR - segL < 2:
                
                res.append(total_ones)
                continue
                
            max_gain = 0
            max_gain = max(max_gain, eval_seg(segL + 1, L, R, segL, segR))
            max_gain = max(max_gain, eval_seg(segR - 1, L, R, segL, segR))
            
            if segL + 2 <= segR - 2:
                max_gain = max(max_gain, query_rmq(segL + 2, segR - 2))
                
            res.append(total_ones + max_gain)
            
        return res