// 11948. 과목선택
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int a,b,c,d,e,f;
  cin >> a >> b >> c >> d >> e >> f;
  int ans = a + b + c + d + e + f;
  ans -= (min({a,b,c,d}) + min(e,f));
  cout << ans;
}