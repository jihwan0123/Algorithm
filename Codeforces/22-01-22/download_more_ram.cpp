// A. Download More RAM
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int a[102], b[102];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)
      v.push_back({a[i], b[i]});
    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++) {
      if (k < v[i].X) break;
      k += v[i].Y;
    }
    cout << k << '\n';
  }
}