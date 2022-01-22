// 1026. 보물
#include <bits/stdc++.h>
using namespace std;
int a[51], b[51];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  sort(a, a + n);
  sort(b, b + n, greater<>());
  int ans = 0;
  for (int i = 0; i < n; i++)
    ans += a[i] * b[i];
  cout << ans;
}