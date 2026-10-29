#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    
    // w[L][R] 记录恰好覆盖区间 [L, R] 的最小代价
    vector<vector<long long>> w(n + 2, vector<long long>(n + 2, INF));
    
    for (int i = 0; i < m; ++i) {
        int l, r;
        long long c;
        cin >> l >> r >> c;
        w[l][r] = min(w[l][r], c);
    }
    
    // 将大区间的代价传递给其内部的子区间
    for (int len = n; len >= 1; --len) {
        for (int l = 1; l + len - 1 <= n; ++l) {
            int r = l + len - 1;
            if (l < r) {
                w[l+1][r] = min(w[l+1][r], w[l][r]);
                w[l][r-1] = min(w[l][r-1], w[l][r]);
            }
        }
    }
    
    // cost[L][R] 表示覆盖连续段 [L, R] 的最小代价
    vector<vector<long long>> cost = w;
    
    // 区间DP计算任意一段连续点的最小覆盖耗费
    for (int len = 2; len <= n; ++len) {
        for (int l = 1; l + len - 1 <= n; ++l) {
            int r = l + len - 1;
            for (int x = l; x < r; ++x) {
                if (cost[l][x] != INF && cost[x+1][r] != INF) {
                    cost[l][r] = min(cost[l][r], cost[l][x] + cost[x+1][r]);
                }
            }
        }
    }
    
    // dp[i][j] 表示前 i 个点中，至少覆盖 j 个点的最小耗费
    vector<vector<long long>> dp(n + 2, vector<long long>(k + 2, INF));
    dp[0][0] = 0;
    
    for (int i = 1; i <= n; ++i) {
        // 情况1：不覆盖第 i 个点
        for (int j = 0; j <= k; ++j) {
            dp[i][j] = min(dp[i][j], dp[i-1][j]);
        }
        
        // 情况2：覆盖一个以 i 结尾的连续段 [l, i]
        for (int l = 1; l <= i; ++l) {
            if (cost[l][i] == INF) continue;
            int num_points = i - l + 1;
            for (int j = 0; j <= k; ++j) {
                if (dp[l-1][j] != INF) {
                    int next_j = min(k, j + num_points);
                    dp[i][next_j] = min(dp[i][next_j], dp[l-1][j] + cost[l][i]);
                }
            }
        }
    }
    
    // 输出结果
    if (dp[n][k] == INF) {
        cout << -1 << "\n";
    } else {
        cout << dp[n][k] << "\n";
    }
}

int main() {
    // 优化输入输出流
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        for (int i = 0; i < t; ++i) {
            cout << "case #" << i << ":\n";
            solve();
        }
    }
    return 0;
}
