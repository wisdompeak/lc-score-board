int _(int s, vector<int>& v, int e, int l, int r, int i) {
  return l <= s && r >= e ? v[i] : e < l || s > r ? 2147483647 : min(_(s, v, s + (e - s) / 2, l, r, 2 * i + 1), _(s + (e - s) / 2 + 1, v, e, l, r, 2 * i + 2));
}

void _(vector<int>& v, int s, int e, int j, int t, int i) {
  if (j >= s && j <= e)
    if (s == e)
      v[i] = t;
    else {
      if (j >= s && j <= s + (e - s) / 2)
        _(v, s, s + (e - s) / 2, j, t, 2 * i + 1);
      else
        _(v, s + (e - s) / 2 + 1, e, j, t, 2 * i + 2);
      v[i] = min(v[2 * i + 1], v[2 * i + 2]);
    }
}

int _(vector<int>& a, int s, int e, vector<int>& v, int i) {
  return v[i] = s == e ? a[s] : min(_(a, s, s + (e - s) / 2, v, i * 2 + 1), _(a, s + (e - s) / 2 + 1, e, v, i * 2 + 2));
}

bool solve(vector<int>&a, vector<int>&b) {
  if (!a.empty()) {
    vector<int> v(2 * (int) pow(2, (int) ceil(log2(a.size()))) - 1);
    _(a, 0, a.size() - 1, v, 0);
    unordered_map<int, int> m1, m2;
    unordered_map<int, vector<int>> m3;
    for (int i = 0; i < a.size(); i++) {
      m1[a[i]]++;
      m3[a[i]].emplace_back(i);
    }
    for (int i : b) {
      if (--m1[i] < 0 || i != _(0, v, a.size() - 1, 0, m3[i][m2[i]], 0))
        return false;
      _(v, 0, a.size() - 1, m3[i][m2[i]++], 2147483647, 0);
    }
  }
  return true;
}

