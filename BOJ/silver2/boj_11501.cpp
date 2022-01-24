// 11501. 주식
#include <bits/stdc++.h>
using namespace std;
int a[1000005];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    // 뒤에서부터 확인
    int cur = a[n];
    long long ans = 0;
    while (--n) {
      if (a[n] > cur) cur = a[n];
      else ans += cur - a[n];
    }
    cout << ans << '\n';
  }
}