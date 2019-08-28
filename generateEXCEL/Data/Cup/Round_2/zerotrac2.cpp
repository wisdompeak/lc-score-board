int lowbit(int x) {
    return x & (-x);
}

void update1(vector<int>& tree, int num, int x, int n) {
    while (x <= n) {
        tree[x] = min(tree[x], num);
        x += lowbit(x);
    }
}

void update2(vector<int>& tree, const vector<int>& a, int x, int n) {
    while (x <= n) {
        tree[x] = a[x - 1];
        int lbit = lowbit(x);
        for (int i = 1; i < lbit; i <<= 1) {
            tree[x] = min(tree[x], tree[x - i]);
        }
        x += lbit;
    }
}

int query(const vector<int>& tree, int x, int n) {
    int ret = n * 2 + 215;
    while (x) {
        ret = min(ret, tree[x]);
        x -= lowbit(x);
    }
    return ret;
}

bool solve(vector<int>& a, vector<int>& b) {
    int n = a.size();
    // keng die de leetcode
    if (n == 0) {
        return true;
    }

    // li san hua
    vector<int> q(a);
    sort(q.begin(), q.end());
    for (int i = 0; i < n; ++i) {
        a[i] = lower_bound(q.begin(), q.end(), a[i]) - q.begin();
    }
    for (int i = 0; i < n; ++i) {
        auto iter = lower_bound(q.begin(), q.end(), b[i]);
        if (iter == q.end() || *iter != b[i]) {
            return false;
        }
        b[i] = iter - q.begin();
    }

    // for (int i = 0; i < n; ++i) cout << a[i] << " "; cout << "\n";
    // for (int i = 0; i < n; ++i) cout << b[i] << " "; cout << "\n";
    
    // dui lie
    unordered_map<int, queue<int>> usq;
    for (int i = 0; i < n; ++i) {
        usq[a[i]].push(i);
    }

    // shu zhuang shu zu
    int verybignumber = n * 2 + 215;
    vector<int> tree(n + 1, verybignumber);
    for (int i = 0; i < n; ++i) {
        update1(tree, a[i], i + 1, n);
    }

    // check
    for (int i = 0; i < n; ++i) {
        queue<int>& q = usq[b[i]];
        if (q.empty()) {
            return false;
        }
        // cout << "check " << i << " start\n";
        int pos = q.front();
        q.pop();
        int prefixmin = query(tree, pos + 1, n);
        // cout << "min = " << prefixmin << " " << b[i] << "\n";
        if (prefixmin != b[i]) {
            return false;
        }
        a[pos] = verybignumber;
        update2(tree, a, pos + 1, n);
        // cout << "tree: "; for (int j = 1; j <= n; ++j) cout << tree[j] << " "; cout << "\n";
    }
    return true;
}
