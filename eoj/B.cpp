#include <bits/stdc++.h>

using namespace std;

bool isSBT(const vector<int>& a) {
    int low = INT_MAX, high = INT_MIN;
    for (int x : a) {
        low = min(low, x);
        high = max(high, x);
        if (low < 10 || high > 30 || high - low > 3) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    while (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        if (isSBT(a)) cout << "Is SBT" << endl;
        else cout << "Is not SBT" << endl;
    }
    return 0;
}