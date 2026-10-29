#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;

struct Item {
    int a, b, c;
    long long w, dp;
};

int n;
Item items[MAXN];
vector<int> c_vals;

// 树状数组维护前缀最大值
struct FenwickTree {
    long long tree[MAXN * 2];
    int n;

    void init(int n) {
        this->n = n;
        for (int i = 0; i <= n; i++) tree[i] = 0;
    }

    void update(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) {
            if (tree[idx] < val) tree[idx] = val;
        }
    }

    long long query(int idx) {
        long long res = 0;
        for (; idx > 0; idx -= idx & -idx) {
            if (res < tree[idx]) res = tree[idx];
        }
        return res;
    }

    void clear(int idx) {
        for (; idx <= n; idx += idx & -idx) {
            tree[idx] = 0;
        }
    }
} bit;

bool cmpB(const Item& x, const Item& y) {
    if (x.b != y.b) return x.b < y.b;
    return x.c < y.c;
}

int ord[MAXN];  // right half in b order (indices), keeps the right half in a order

void cdq(int l, int r) {
    if (l >= r) return;

    // 寻找 a 值的严格边界，防止 a 相同导致交叉转移
    int mid = (l + r) / 2;
    while (mid < r && items[mid].a == items[mid + 1].a) mid++;
    if (mid == r) {
        mid = (l + r) / 2;
        while (mid > l && items[mid].a == items[mid + 1].a) mid--;
    }

    // 如果当前区间所有的 a 都相同，则内部无法产生转移
    if (items[l].a == items[r].a) return;

    // 先递归左边，此时左半部分的 dp 已经确定
    cdq(l, mid);

    // 左半部分之后不会再被递归，直接按 b 排序
    sort(items + l, items + mid + 1, cmpB);

    // 右半部分还要继续递归，必须保持 a 有序，所以只对下标副本按 b 排序
    int m = r - mid;
    for (int k = 0; k < m; k++) ord[k] = mid + 1 + k;
    sort(ord, ord + m, [](int x, int y) {
        if (items[x].b != items[y].b) return items[x].b < items[y].b;
        return items[x].c < items[y].c;
    });

    // 用左半部分更新右半部分
    int i = l;
    for (int k = 0; k < m; k++) {
        int j = ord[k];
        while (i <= mid && items[i].b < items[j].b) {
            bit.update(items[i].c, items[i].dp);
            i++;
        }
        long long max_dp = bit.query(items[j].c - 1);
        items[j].dp = max(items[j].dp, max_dp + items[j].w);
    }

    // 撤销树状数组的修改，保证回溯时树状数组干净
    for (int k = l; k < i; k++) {
        bit.clear(items[k].c);
    }

    // 右半部分已经拿到左半部分的贡献，再递归处理内部转移
    cdq(mid + 1, r);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> items[i].a >> items[i].b >> items[i].c >> items[i].w;
        items[i].dp = items[i].w; // dp初始化为自身的重量
        c_vals.push_back(items[i].c);
    }

    // 离散化 c 坐标
    sort(c_vals.begin(), c_vals.end());
    c_vals.erase(unique(c_vals.begin(), c_vals.end()), c_vals.end());

    for (int i = 0; i < n; i++) {
        items[i].c = lower_bound(c_vals.begin(), c_vals.end(), items[i].c) - c_vals.begin() + 1;
    }

    // 初始排序，以 a 为第一关键字升序
    sort(items, items + n, [](const Item& x, const Item& y) {
        if (x.a != y.a) return x.a < y.a;
        if (x.b != y.b) return x.b < y.b;
        return x.c < y.c;
    });

    bit.init(c_vals.size() + 1);

    // CDQ 分治
    cdq(0, n - 1);

    long long ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, items[i].dp);
    }

    cout << ans << "\n";

    return 0;
}
