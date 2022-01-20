// 11047. 동전 0
#include <bits/stdc++.h>
using namespace std;
int a[11];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, k;
  int ans = 0;
  cin >> n >> k;
  for (int i = 1; i <= n; i++)
    cin >> a[i];

  while (k) {
    ans += (k / a[n]);
    k %= a[n];
    n--;
  }
  cout << ans;
}