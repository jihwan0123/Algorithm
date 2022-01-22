// 2217. 로프
#include <bits/stdc++.h>
using namespace std;
int a[100005];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
  sort(a + 1, a + n + 1, greater<>());
  int ans = 0;
  for (int i = 1; i <= n; i++)
    ans = max(ans, a[i] * i);

  cout << ans;
}