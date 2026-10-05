#include <bits/stdc++.h>

using namespace std;
using ll = long long;

void printSet(const set<ll>& s) {
    cout << "{";
    for (auto it = s.begin(); it != s.end(); ++it) {
        cout << *it;
        if (next(it) != s.end()) cout << ",";
    }
    cout << "}" << endl;
}

int main() {
    int n, m; cin >> n >> m;
    set<ll> a, b;
    for (int i = 0; i < n; ++i) {
        ll x; cin >> x;
        a.insert(x);
    }
    for (int i = 0; i < m; ++i) {
        ll x; cin >> x;
        b.insert(x);
    }
    set<ll> c, d, e;
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(c, c.begin()));
    set_union(a.begin(), a.end(), b.begin(), b.end(), inserter(d, d.begin()));
    set_difference(a.begin(), a.end(), b.begin(), b.end(), inserter(e, e.begin()));

    printSet(c);
    printSet(d);
    printSet(e);

    return 0;
}