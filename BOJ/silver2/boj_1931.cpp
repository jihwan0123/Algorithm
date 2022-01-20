// 1931. 회의실배정
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<pair<int, int>> v;
  for (int i = 0; i < n; i++) {
    int s, e;
    cin >> s >> e;
    v.push_back({e, s});
  }
  sort(v.begin(), v.end());
  int st = 0, en = v[st].X;
  int ans = 1;
  while (st < n) {
    if (v[st + 1].Y >= en) {
      ans++;
      en = v[st + 1].X;
    }
    st++;
  }
  cout << ans;
}