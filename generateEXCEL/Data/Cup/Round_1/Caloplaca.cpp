int _(string& s, int i, int j) {
  if (i < s.size() && s[i] == j)
    return i + 1;
  for (int k = i, l = 0; k > 0; k--)
    if (s[k - 1] == j) {
      for (l = 0; l < k - 1; l++)
        if (s[l] != s[i - k + l + 1])
          break;
      if (l == k - 1)
        return k;
    }
  return 0;
}

void _(string& s, vector<vector<int>>& S) {
  for (int i = 0; i <= s.size(); i++)
    for (int j = 'a'; j <= 'z'; j++)
      S[i][j - 'a'] = _(s, i, j);
}

int _(int i, int j, int k, string& u, string& s, string& t, vector<vector<vector<int>>>& dp, vector<vector<int>>& S, vector<vector<int>>& T) {
  if (i == u.size())
    return 0;
  if (dp[i][j][k] == -999999)
    for (int c = u[i] == '*' ? 'a' : u[i]; c <= (u[i] == '*' ? 'z': u[i]); c++)
      dp[i][j][k] = max(dp[i][j][k], _(i + 1, S[j][c - 'a'], T[k][c - 'a'], u, s, t, dp, S, T) + (S[j][c - 'a'] == s.size()) - (T[k][c - 'a'] == t.size()));
  return dp[i][j][k];
}

int solve(string u, string s, string t) {
  vector<vector<vector<int>>> dp(u.size(), vector<vector<int>>(s.size() + 1, vector<int>(t.size() + 1, -999999)));
  vector<vector<int>> S(s.size() + 1, vector<int>(26)), T(t.size() + 1, vector<int>(26));
  _(s, S);
  _(t, T);
  return _(0, 0, 0, u, s, t, dp, S, T);
}
