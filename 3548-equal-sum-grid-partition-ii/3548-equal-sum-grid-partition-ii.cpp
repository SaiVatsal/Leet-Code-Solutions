#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long total_sum = 0;
        
        vector<long long> row_sum(m, 0);
        vector<long long> col_sum(n, 0);
        
        const int MAX_VAL = 100005;
        vector<int> min_row(MAX_VAL, 1e9), max_row(MAX_VAL, -1e9);
        vector<int> min_col(MAX_VAL, 1e9), max_col(MAX_VAL, -1e9);
        
        // Precompute sums and boundary boxes for O(1) existence checks
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                total_sum += val;
                row_sum[i] += val;
                col_sum[j] += val;
                
                if (val < MAX_VAL) {
                    min_row[val] = min(min_row[val], i);
                    max_row[val] = max(max_row[val], i);
                    min_col[val] = min(min_col[val], j);
                    max_col[val] = max(max_col[val], j);
                }
            }
        }
        
        // Evaluate Horizontal Cuts
        long long top_sum = 0;
        for (int i = 0; i < m - 1; ++i) {
            top_sum += row_sum[i];
            long long bot_sum = total_sum - top_sum;
            long long D = top_sum - bot_sum;
            
            if (D == 0) return true;
            
            if (D > 0 && D < MAX_VAL) {
                int rows = i + 1, cols = n;
                if (rows >= 2 && cols >= 2) {
                    if (min_row[D] <= i) return true; 
                } else {
                    if (grid[0][0] == D || grid[0][n-1] == D || grid[i][0] == D || grid[i][n-1] == D) return true;
                }
            } else if (D < 0 && -D < MAX_VAL) {
                long long target = -D;
                int rows = m - 1 - i, cols = n;
                if (rows >= 2 && cols >= 2) {
                    if (max_row[target] >= i + 1) return true; 
                } else {
                    if (grid[i+1][0] == target || grid[i+1][n-1] == target || grid[m-1][0] == target || grid[m-1][n-1] == target) return true;
                }
            }
        }
        
        // Evaluate Vertical Cuts
        long long left_sum = 0;
        for (int j = 0; j < n - 1; ++j) {
            left_sum += col_sum[j];
            long long right_sum = total_sum - left_sum;
            long long D = left_sum - right_sum;
            
            if (D == 0) return true;
            
            if (D > 0 && D < MAX_VAL) {
                int rows = m, cols = j + 1;
                if (rows >= 2 && cols >= 2) {
                    if (min_col[D] <= j) return true; 
                } else {
                    if (grid[0][0] == D || grid[0][j] == D || grid[m-1][0] == D || grid[m-1][j] == D) return true;
                }
            } else if (D < 0 && -D < MAX_VAL) {
                long long target = -D;
                int rows = m, cols = n - 1 - j;
                if (rows >= 2 && cols >= 2) {
                    if (max_col[target] >= j + 1) return true; 
                } else {
                    if (grid[0][j+1] == target || grid[0][n-1] == target || grid[m-1][j+1] == target || grid[m-1][n-1] == target) return true;
                }
            }
        }
        
        return false;
    }
};