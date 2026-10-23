#include <bits/stdc++.h>

using namespace std;
using ll = long long;

void solution(int t) {
    ll A; cin >> A;

    cout << "case #" << t << ":\n";

    auto s = to_string(A);
    auto len = s.length();

    vector<ll> seq;
    for (char c : s) {
        seq.push_back(c - '0');
    }

    if (A <= len) {
        ll sum = 0;
        for (ll i = 0; i < A; ++i) sum += seq[i];
        cout << sum << endl;
        return;
    }

    int pos[10][10][10];
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < 10; ++k) {
                pos[i][j][k] = -1;
            }
        }
    }

    ll current_len = len;
    ll current_sum = 0;
    for (int x : seq) current_sum += x;

    pos[seq[len-3]][seq[len-2]][seq[len-1]] = current_len;

    vector<ll> prefix_sum;
    prefix_sum.push_back(0);
    for (size_t i = 0; i < len; ++i) {
        prefix_sum.push_back(prefix_sum.back() + seq[i]);
    }

    while (current_len < A) {
        int next_digit = (seq[current_len-3] + seq[current_len-2]) * seq[current_len-1] % 10;
        seq.push_back(next_digit);
        current_sum += next_digit;
        prefix_sum.push_back(prefix_sum.back() + next_digit);
        ++current_len;

        if (current_len == A) {
            cout << current_sum << endl;
            return;
        }

        int a = seq[current_len-3];
        int b = seq[current_len-2];
        int c = seq[current_len-1];

        if (pos[a][b][c] != -1) {
            ll start_len = pos[a][b][c];
            ll loop_len = current_len - start_len;

            ll loop_sum = prefix_sum[current_len] - prefix_sum[start_len];

            ll rem_len = A - current_len;
            ll num_loops = rem_len / loop_len;
            ll rem_part = rem_len % loop_len;

            ll total_sum = current_sum;
            total_sum += num_loops * loop_sum;
            total_sum += prefix_sum[start_len + rem_part] - prefix_sum[start_len];

            cout << total_sum << endl;
            return;
        } else {
            pos[a][b][c] = current_len;
        }
    }
    cout << current_sum << endl;
}

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; ++t) {
        solution(t);
    }
    return 0;
}
