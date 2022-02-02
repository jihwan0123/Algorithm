// 4796. 캠핑
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t = 0;
  while (++t) {
    int l, p, v;
    cin >> l >> p >> v;
    if (l==0 && p==0 && v==0) break;
    int ans = 0;
    int x = v / p;
    ans = x * l + min(v - x * p, l);
    cout << "Case " << t << ": " << ans << '\n';
  }
}