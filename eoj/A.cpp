#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    int n; cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    ll d = 2, diff = 0;
    for (int i = 1; i < n; ++i) {
        diff += d;
        a[i] -= diff;
        ++d;
    }

    int mid = n / 2;
    nth_element(a.begin(), a.begin() + mid, a.end());
    ll median = a[mid];

    ll ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += abs(a[i] - median);
    }

    cout << ans << endl;

    return 0;
}