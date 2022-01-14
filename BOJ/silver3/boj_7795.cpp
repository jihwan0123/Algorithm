// 7795. 먹을 것인가 먹힐 것인가
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

bool cmp(const pair<int, int> &a, const pair<int, int> &b) { 
  return a.X > b.X;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n, m, x;
    cin >> n >> m;
    vector<pair<int, int>> arr; // pair : {x, cnt}
    for (int i = 0; i < n; i++) {
      cin >> x;
      bool chk = true;
      for (auto &a : arr) {
        if (x == a.X) {
          a.Y++;
          chk = false;
          break;
        }
      }
      if (chk)
        arr.push_back({x, 1});
    }

    sort(arr.begin(), arr.end(), cmp);

    int ans = 0;
    for (int i = 0; i < m; i++) {
      cin >> x;
      for (auto &b : arr) {
        if (b.X <= x)
          break;
        ans += b.Y;
      }
    }
    cout << ans << '\n';
  }
}