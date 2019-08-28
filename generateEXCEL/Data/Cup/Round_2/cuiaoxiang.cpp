#define _USE_MATH_DEFINES
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <complex>
#include <cmath>
#include <numeric>
#include <bitset>
#include <functional>
#include <random>
#include <ctime>

using namespace std;

#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << ": " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << ": " << arg1 << " |";
  __f(comma + 1, args...);
}

typedef long long int64;
typedef pair<int, int> ii;
const int INF = 1 << 29;
const int MOD = 1e9 + 7;

const int N = 1e5 + 10;

struct Node {
  Node *left, *right;
  int a, b;
  int minv;
  void pushup() {
    minv = min(left->minv, right->minv);
  }
};

Node pool[N << 1], *last;

Node* new_node(int a, int b) {
  Node* cur = last++;
  cur->a = a;
  cur->b = b;
  return cur;
}

Node* build(const vector<int>& A, int a, int b) {
  Node* cur = new_node(a, b);
  if (a + 1 == b) {
    cur->minv = A[a];
    return cur;
  }
  cur->left = build(A, a, (a + b) / 2);
  cur->right = build(A, (a + b) / 2, b);
  cur->pushup();
  return cur;
}

int A, B;
void update(Node* cur) {
  if (cur->a + 1 == cur->b) {
    cur->minv = B;
    return;
  }
  if ((cur->a + cur->b) / 2 > A) update(cur->left);
  else update(cur->right);
  cur->pushup();
}

int query(Node* cur) {
  if (cur->a >= A && cur->b <= B) {
    return cur->minv;
  }
  int ret = numeric_limits<int>::max();
  if ((cur->a + cur->b) / 2 > A) ret = min(ret, query(cur->left));
  if ((cur->a + cur->b) / 2 < B) ret = min(ret, query(cur->right));
  return ret;
}

bool solve(vector<int>& a, vector<int>& b) {
  int n = a.size();
  unordered_map<int, vector<int>> q;
  for (int i = n - 1; i >= 0; --i) {
    q[a[i]].push_back(i);
  }
  last = pool;
  Node* root = build(a, 0, n);
  for (int i = 0; i < n; ++i) {
    if (q[b[i]].empty()) return false;
    int k = q[b[i]].back();
    q[b[i]].pop_back();
    A = 0, B = k;
    int best = query(root);
    // trace(i, k, best);
    if (best < a[k]) return false;
    A = k, B = numeric_limits<int>::max();
    update(root);
  }
  return true;
}

int main() {
  int cas;
  scanf("%d", &cas);
  while (cas--) {
    int n;
    scanf("%d", &n);
    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; ++i) {
      scanf("%d", &b[i]);
    }
    bool ret = solve(a, b);
    puts(ret ? "YES" : "NO");
  }
  return 0;
}
