// 11399. ATM
#include <bits/stdc++.h>
using namespace std;
int a[1001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a, a + n);
  int ans = a[0];
  for (int i = 1; i < n; i++) {
    a[i] += a[i - 1];
    ans += a[i];
  }
  cout << ans;
}