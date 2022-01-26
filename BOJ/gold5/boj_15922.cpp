// 15922. 아우으 우아으이야!!
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<pair<int,int>> lines;
  for (int i=0; i<n; i++){
    int x, y;
    cin >> x >> y;
    lines.push_back({x, y});
  }
  int l, r;
  tie(l, r) = lines[0];
  int ans = 0;
  for (int i=1; i<n; i++) {
    int a, b;
    tie(a, b) = lines[i];
    if (a <= r && b >= r) r = b;
    else if (a > r) {
      ans += r - l;
      l = a;
      r = b;
    }
  }
  cout << ans + r - l;
}