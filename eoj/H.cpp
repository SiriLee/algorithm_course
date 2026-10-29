#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

// dp[i][j] 表示剩余 i 份玉米和 j 份葡萄时，玉米先卖完（提前打烊）的概率
double dp[2005][2005];

void precompute() {
    for (int i = 0; i <= 2000; ++i) {
        for (int j = 0; j <= 2000; ++j) {
            if (i == 0 && j > 0) {
                dp[i][j] = 1.0; // 玉米先卖完
            } else if (i == 0 && j == 0) {
                dp[i][j] = 0.0; // 同时卖完，不打烊
            } else if (i > 0 && j == 0) {
                dp[i][j] = 0.0; // 葡萄先卖完，玉米最后也会卖完，不打烊
            } else {
                double sum = 0.0;
                int cnt = 0;
                // 检查五种套餐是否可行
                if (i >= 4) { sum += dp[i-4][j]; cnt++; }             // 1 份玉米
                if (i >= 3 && j >= 1) { sum += dp[i-3][j-1]; cnt++; } // 3/4 玉米 + 1/4 葡萄
                if (i >= 2 && j >= 2) { sum += dp[i-2][j-2]; cnt++; } // 1/2 玉米 + 1/2 葡萄
                if (i >= 1 && j >= 3) { sum += dp[i-1][j-3]; cnt++; } // 1/4 玉米 + 3/4 葡萄
                if (j >= 4) { sum += dp[i][j-4]; cnt++; }             // 1 份葡萄
                
                if (cnt > 0) {
                    dp[i][j] = sum / cnt;
                } else {
                    dp[i][j] = 0.0;
                }
            }
        }
    }
}

int main() {
    // 优化 I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 预处理 DP 表
    precompute();

    int n, m;
    while (cin >> n >> m) {
        // 由于初始乘了 4，所以对应的状态是 4*n 和 4*m
        cout << fixed << setprecision(10) << dp[4 * n][4 * m] << "\n";
    }

    return 0;
}
