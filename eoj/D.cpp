#include <bits/stdc++.h>

using namespace std;
using ll = long long;

string normalize(const string& s) {
    auto len = s.length();
    if (len % 2 == 1 || len == 0) {
        return s;
    }

    auto half = len / 2;
    auto left = normalize(s.substr(0, half));
    auto right = normalize(s.substr(half, half));

    if (left > right) {
        return right + left;
    }
    return left + right;
}

int main() {
    string s1, s2;
    cin >> s1 >> s2;

    if (s1.length() != s2.length()) {
        cout << "No" << endl;
        return 0;
    }

    auto s1_norm = normalize(s1);
    auto s2_norm = normalize(s2);

    if (s1_norm == s2_norm) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
